from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import csv
import requests
from youtube_search import YoutubeSearch
import cx_Oracle
#pip install youtube-search

def getPageLinksWantRange(startPageNo, lastPageNo): 
    links = [] 
    return_links = [] 
    for pageNo in range(startPageNo-1, lastPageNo): 
        url = "https://series.naver.com/movie/recentList.nhn?orderType=sale&sortingType=&tagCode=&page=" + str(pageNo + 1) 
        req = requests.get(url) 
        soup = bs(req.text, 'lxml') 
        movielinks = soup.select('div.lst_thum_wrap ul li a[href]') 
        for movielink in movielinks: 
            link = str(movielink.get('href')) 
            links.append("https://series.naver.com"+link) 
    return links

def getMovieDataFromNaverSeries(links):
    genrelist = []
    res = requests.get(links) # 이 주소로 저 서버에세 get방식으로 요청
    res.raise_for_status
    res.close()
     
    soup = bs(res.text,'lxml') #이 글자를 lxml로 해석해줘
    title = soup.find("span",attrs={'class','pic_area'}).find("img")['alt'] #좌측에 있는 조그마한 이미지의 alt값에서 제목 가져옴
     
    return title

for i in range(500):
    try:
        print("=================================")
        title = getMovieDataFromNaverSeries(getPageLinksWantRange(1,20)[i])
        search = title+'리뷰'
        r_results = YoutubeSearch(search, max_results=10).to_dict() #유튜브 검색을 딕셔너리로 뽑음 
        print(search)
        for i in r_results:
            r_url = i['url_suffix'] #url 주소를 뽑음 
            r_title = i['title']    #title을 뽑음 
            r_thumbnails = i['thumbnails'] #thumbnails 뽑음
            r_href = 'https://www.youtube.com/'+r_url  #유튜브 url 그대로 가져옴 , 댓글이랑 다른게 다뜸
            # print(r_title)
            # print(r_href)
            # print(r_thumbnails[-1])
            # print("https://www.youtube.com/embed/"+r_url.split("v=")[-1]+"?autoplay=0") 
            youtube = {'title':r_title,'thum' :r_thumbnails[-1],'url':"https://www.youtube.com/embed/"+r_url.split("v=")[-1]+"?autoplay=0" }
            print(youtube)
            youtube[title] =r_title,r_thumbnails[-1],"https://www.youtube.com/embed/"+r_url.split("v=")[-1]+"?autoplay=0"

    except AttributeError:
        print("19금 >_<")


# with open('youtube4.csv','w',encoding='utf-8') as f:
#     w = csv.writer(f)
#     w.writerow(youtube.keys())
#     w.writerow(youtube.values())




