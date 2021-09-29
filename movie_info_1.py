from bs4 import BeautifulSoup as bs
import requests
from cx_Oracle import DatabaseError
from selenium import webdriver
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time
import re
import cx_Oracle
import time


class Movie:
    def __init__(self):
        self.MOVIETITLE = ""
        self.MOVIECODE = ""
        self.MOVIEPLOT = ""
        self.MOVIEMODE = ""
        self.MOVIEPRICE = ""
        self.MOVIEPOSTRIMG = ""
        self.MOVIEDIRECTOR = ""
        self.MOVIEGENRE = ""


def getConn():
    # conn = cx_Oracle.connect("scott", "scott1234!", "orcl.cu1tbymhc2wb.ap-northeast-2.rds.amazonaws.com:1521/orcl")
    return cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")


def getPageLinksWantRange(startPageNo, lastPageNo):
    links = []
    codes = []

    for pageNo in range(startPageNo-1, lastPageNo):
        url = "https://series.naver.com/movie/recentList.nhn?orderType=sale&sortingType=&tagCode=&page=" + str(pageNo + 1)
        req = requests.get(url)
        soup = bs(req.text, 'lxml')
        movielinks = soup.select('div.lst_thum_wrap ul li a[href]')
        for movielink in movielinks:
            link = str(movielink.get('href'))
            links.append("https://series.naver.com"+link)
            codes.append(link.split("=")[1])

    return links


broswer = webdriver.Chrome("../../chromedriver.exe")

def getMovieDataFromNaverSeries(links):
    print("---------- BEGIN CODE ----------")
    code = links.split("=")[1]

    res = requests.get(links) # 이 주소로 저 서버에세 get방식으로 요청
    res.raise_for_status
    res.close()

    soup = bs(res.text, 'lxml') #이 글자를 lxml로 해석해줘

    dirs = soup.find("li", attrs={'class', 'info_lst'}).find_all("a", attrs={'class', 'NPI=a:plink'})
    dirr=[]
    for a in dirs:
        dirr.append(a.get_text())

    genre = soup.find("li", attrs={"class", "info_lst"}).find("a").get_text()
    price = soup.find("strong", attrs={'class', 'payment'}).get_text()
    title = soup.find("span", attrs={'class', 'pic_area'}).find("img")['alt']  # 좌측에 있는 조그마한 이미지의 alt값에서 제목 가져옴
    mvpst = soup.find("span", attrs={'class', 'pic_area'}).find("img")['src']  # 위 값을 가져온 이미지의 src를 가져옴
    mode = soup.find("span", attrs={'class', 'tit tit_buy'}).get_text()
    # tit tit_buy

    broswer.get(links)
    reviewList = []
    plot = ""
    plotText = ""

    try:
        plotBtn = broswer.find_element_by_xpath('//*[@id="content"]/div[4]/span/a')
        plotBtn.click()

        try:
            plot = broswer.find_element_by_xpath('//*[@id="content"]/div[5]')
            plotText = plot.text.strip()
        except:
            print("plot error")
            errorFlag = True

    except:
        plot = broswer.find_element_by_xpath('//*[@id="content"]/div[4]')
        plotText = plot.text.strip().replace("'", "''")
        errorFlag = True
        # print(plotText)

    # print("plotText len :", len(plotText))
    plotTextlen = len(plotText)
    slicedPlotText = ""
    if plotTextlen > 1800:
        slicedPlotText = plotText[:1700]
    else:
        slicedPlotText = plotText

    try:
        index = 1
        for e in range(1, 5):
            review = broswer.find_element_by_xpath('//*[@id="cbox_module"]/div/div[5]/ul/li[' + str(index) + ']/div[1]/div/div[2]')
            index += 1
            reviewList.append(review.text)
    except:
        print("error")
        errorFlag =True

    director = dirr[0]
    castList = dirr[1:]

    conn = getConn()
    cur = conn.cursor()

    testMovie = Movie()
    testMovie.MOVIETITLE = title
    testMovie.MOVIECODE = code
    testMovie.MOVIEPLOT = slicedPlotText
    testMovie.MOVIEMODE = mode
    testMovie.MOVIEPRICE = price
    testMovie.MOVIEPOSTERIMG = mvpst
    testMovie.MOVIEDIRECTOR = director
    testMovie.MOVIEGENRE = genre

    sql = """ INSERT INTO MOVIE VALUES (MOVIE_SEQ.NEXTVAL,"""
    sql += "'" + testMovie.MOVIETITLE + "',"
    sql += "'" + testMovie.MOVIECODE + "',"
    sql += "'" + testMovie.MOVIEPLOT + "',"
    sql += "'" + testMovie.MOVIEMODE + "',"
    sql += "'" + testMovie.MOVIEPRICE + "',"
    sql += "'" + testMovie.MOVIEPOSTERIMG + "',"
    sql += "'" + testMovie.MOVIEDIRECTOR + "',"
    sql += "'" + testMovie.MOVIEGENRE + "'"
    sql += ")"



    try:
        cur.execute(sql)
    except DatabaseError as dberror:
        print("---------- ERROR ----------")
        print("MOVIETITLE :", testMovie.MOVIETITLE)
        print("MOVIEPLOT :", testMovie.MOVIEPLOT)
        errorFlag = True

    sql = "SELECT max(MOVIESEQ) from MOVIE"
    cur.execute(sql)

    lastId = 0
    for d in cur:
        lastId = d[0]
    # print("lastId : ", lastId)
    castId = 0
    # print(castList)
    for cast in castList:
        # print(cast)
        sql = "SELECT COUNT(CASTSEQ) FROM CAST WHERE CASTNAME = '"+cast+"'"
        cur.execute(sql)
        count = 0
        for d in cur:
            count = d[0]
        # print("count :", count)
        if count < 1:
            sql = "INSERT INTO CAST VALUES (CAST_SEQ.nextval, '"+cast+"')"
            cur.execute(sql)
            sql = "SELECT max(CASTSEQ) from CAST"
            cur.execute(sql)
            for d in cur:
                castId = d[0]
        else:
            sql = "SELECT CASTSEQ FROM CAST WHERE CASTNAME = '" + cast + "'"
            cur.execute(sql)
            for d in cur:
                castId = d[0]
        # print("castId : ", castId)
        sql = "INSERT INTO CAST_MOVIE VALUES ("+str(castId)+","+str(lastId)+",CAST_SEQ.nextval)"
        cur.execute(sql)

    for review in reviewList:
        # print(review)

        reviewText = review.strip().replace("'", "''")
        # print("reviewText len :", len(reviewText))
        textlen = len(reviewText)
        slicedReviceText = ""
        if textlen > 200:
            slicedReviceText = reviewText[:199]
        else:
            slicedReviceText = reviewText
        try:
            sql = "INSERT INTO TEXT_REVIEW VALUES (REVIEW_SEQ.nextval,'"+slicedReviceText+"',"+str(lastId)+")"
            cur.execute(sql)
        except DatabaseError as dberror:
            print("---------- ERROR ----------")
            print("error :", dberror)
            print("reviewData :", slicedReviceText)
            errorFlag = True


    # return title, mvpst, price, genre, director, castList, mode
    if errorFlag:
        conn.rollback()
    else:
        conn.commit()

    conn.close()
    print("movieSeq :", lastId)
    print("movieTitle :", testMovie.MOVIETITLE)
    print("---------- DONE ----------")
    # print(reviewList)


    time.sleep(2)
    return errorFlag

for i in range(500):
    try:
        print("========== "+str(i)+" ==========")
        errorFalg = getMovieDataFromNaverSeries(getPageLinksWantRange(1, 20)[i])
        print("========== resut ==========")
        print("errorFalg :", errorFalg)

    except AttributeError:
        print("19금 >_<")



