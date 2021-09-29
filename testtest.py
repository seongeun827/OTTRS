
"""

lastId = 22
castId = 22
sql = "INSERT INTO CAST VALUES ("+str(castId)+","+str(lastId)+",CAST_SEQ.nextval)"
print(sql)

# https://serieson.naver.com/movie/detail.nhn?productNo=2747742
from selenium import webdriver
broswer = webdriver.Chrome("../chromedriver.exe")
broswer.get("https://serieson.naver.com/movie/detail.nhn?productNo=2747742")
try:
    plotBtn = broswer.find_element_by_xpath('//*[@id="content"]/div[4]/span/a')
    plotBtn.click()
except:
    plot = broswer.find_element_by_xpath('//*[@id="content"]/div[4]')
    plotText = plot.text
    print(plotText)
review = ''' BEST그냥 오픈해주지 빨리다른 의미로 신선했다. 2010년 대에 이렇게 노골적으로 눈물 흘리라고 눈을 찌르는 수준의 신파극을 보여줄지 전혀 예상 못했기 때문에. 또한 갑자기 장르가 액션블록버스터로 바뀌며 초사이언이 되어 건물사이사이를 날아다니는 걸 보고 "돈 되는 건 다 섞었구나."했지만, 진짜로 이게 초대박 흥행을 하며 실제로 돈이 되는 걸 보고, 나는 어떤 사업가적인 감동을 느꼈다. 이 영화는 경영학 서적에 어울린다. 이건 기적이다. 영화사는 "돈을 주세요!"라며 이 영화를 만들었고, 실제로 관객들이 돈을 준 것이다! '''
print(type(review))
# reviewText = review.strip().replace("'", "''")
# lastId = 45
print(len(review))

# print("INSERT INTO TEXT_REVIEW VALUES (REVIEW_SEQ.nextval,'"+reviewText+"',"+str(lastId)+")")

from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from selenium import webdriver


url="https://www.youtube.com/feed/storefront?bp=kgEmCGQSIlBMSFBUeFR4dEMwaVpFSkE4TFdrSVVPOTJkVk9aMmVZOWKiBQIoBQ%3D%3D"
browser = webdriver.Chrome("../chromedriver.exe")
browser.get(url)


elems = browser.find_elements_by_id("thumbnail")
for elem in elems:
    print(elem.get_attribute("href"))

# print(elem)
import cx_Oracle
from random import randint

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
        self.MOVIEIMGNAME = ""

def getLotto(maxLength):
    print(maxLength)
    lotto = set()
    while len(lotto) < 15:
        lotto.add(randint(0, maxLength - 1))
    lotto = list(lotto)
    return lotto

def getConn():
    # conn = cx_Oracle.connect("scott", "scott1234!", "orcl.cu1tbymhc2wb.ap-northeast-2.rds.amazonaws.com:1521/orcl")
    return cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")


conn = getConn()
cur = conn.cursor()
sql = "SELECT * FROM MOVIE"
cur.execute(sql)

movieSelectList = [i for i in cur.fetchall()]
movieLen = len(movieSelectList)
randomIndexList = getLotto(movieLen)
print(movieSelectList)
print("movieLen :", movieLen)
print(randomIndexList)
print(movieSelectList[34][0])
print(movieSelectList[34][1])
print(movieSelectList[34][2])
print(movieSelectList[34][3])





# for index in randomIndexList:
#     print(index)
#     print(type(movieSelectList[index]))
#     print(movieSelectList[index])

for idx in range(0, 15):
    print(idx)
import cx_Oracle

conn = cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
cur = conn.cursor()

sql = "SELECT MOVIESEQ, MOVIETITLE FROM MOVIE"
cur.execute(sql)



for d in cur:
    movieSeq = d[0]
    movieTitle = d[1]
    print(movieSeq, movieTitle)


movieSeq = 164
print("movieSeq :", movieSeq)
sql = "SELECT TEXTREVIEWVALUE FROM MOVIE WHERE MOVIESEQ ="+movieSeq
print(sql)

youList = [('uf_365_1.jpg', 'https://www.youtube.com/embed/2aTbyw9ytMU?autoplay=0'), ('uf_365_2.jpg', 'https://www.youtube.com/embed/KEXP8hfUtpo?autoplay=0'), ('uf_365_3.jpg', 'https://www.youtube.com/embed/cc6DSzNjNIY?autoplay=0'), ('uf_365_4.jpg', 'https://www.youtube.com/embed/VXrE--nHqQo?autoplay=0')]
youtubeThumbImgList = [r[0] for r in youList]
youtubeUrlList = [r[1] for r in youList]

for i, yti in enumerate(youtubeThumbImgList):
    print(i,yti )

for i, yti in enumerate(youtubeUrlList):
    print(i,yti )

reviewList = ['BEST가격 확 내려간거 보소 ㅋㅋㅋㅋ', 'BEST스트레스 풀려고봤는데 많이 웃었어요3인방 연기력좋고 김우빈 잘생겼네요 ㅎㅎ', '꿀잼! 한참 웃엇내요오오오 ㅎㅎㅎ', '재밌네요.']
rvText = ""
for rv in reviewList:
    rvText += rv + "\n"

print(rvText)

import cx_Oracle

conn = cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
cur = conn.cursor()

# userEmail="d@d.com"
userEmail="em@naver.com"
sql =
                    SELECT USERSEQ FROM USER_GENRE ug
                    WHERE ug.userSeq = (SELECT USERSEQ FROM OTTRS_USER WHERE USEREMAIL='%s')
                     % userEmail
print("sql :", sql)
cur.execute(sql)
logUserSeq = 0
exFlag = False
for userSeq in cur:
    logUserSeq = userSeq[0]
    exFlag = True
print("-------------------------")
if exFlag:
    print(logUserSeq)
    print("exFlag :", exFlag)

else:
    print(logUserSeq)
    print("exFlag :", exFlag)
conn.close()

from engine_1 import getMovieGenreList

movieList = getMovieGenreList(28)
print(movieList)
"""

import cx_Oracle

conn = cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
cur = conn.cursor()
userEmail = "d@naver.com"

sql = "SELECT USERSEQ FROM OTTRS_USER WHERE USEREMAIL='%s'"%userEmail
print(sql)
cur.execute(sql)
logUserSeq = cur.fetchall()[0][0]
print(logUserSeq)
