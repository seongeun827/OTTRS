import time
from bs4 import BeautifulSoup as bs
import requests
from urllib.request import Request, urlopen


def func_get_movie_list(URL, CATEGORY, Gijun):
    pages = set()

    soup = bs(urlopen(URL), "html.parser", from_encoding='utf-8')
    print(soup)

    LinkListRAW = soup.findAll(class_="style-scope ytd-section-list-renderer")
    print(LinkListRAW)

    for LINK_RAW in LinkListRAW:
        parseLink = LINK_RAW.find("a")
        Link = "https://www.youtube.com" + parseLink.get("href").replace("..", "").replace("./", "", 1)
        Title = parseLink.get("title")
        RAW_Thumbnail = "https://i.ytimg.com/vi/" + parseLink.get("href").replace("/watch?v=", "") + "/hqdefault.jpg"

        print("[영상링크]" + Link)
        print("[제목]" + Title)
        print("[썸네일주소]" + RAW_Thumbnail)


CATEGORY = "Review"
ARMY = ['기생충리뷰', '영화리뷰']  # 해당 문자열 패턴이 있는 영상만 검색

Limit = len(ARMY)
Gijun = 400000  # 월간 40만건 이상 조회수 기록한 글만 크롤링
count = 0

while count < Limit:
    KEY = str(str(ARMY[count]).encode('utf8')).replace("\\x", "%").replace("b'", "")
    print("KEY :", KEY)
    URL = "https://www.youtube.com/results?search_query=" + KEY # 월간
    print(URL)
    func_get_movie_list(URL, CATEGORY, Gijun)
    time.sleep(7)
    count += 1