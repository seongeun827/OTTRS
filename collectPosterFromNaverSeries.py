import requests
import cx_Oracle
from bs4 import BeautifulSoup as bs
from pathlib import Path


def getConn():
    # conn = cx_Oracle.connect("scott", "scott1234!", "orcl.cu1tbymhc2wb.ap-northeast-2.rds.amazonaws.com:1521/orcl")
    return cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")


conn = getConn()
cur = conn.cursor()

sql = "SELECT MOVIEPOSTERIMG, MOVIECODE FROM MOVIE"
cur.execute(sql)
fileDir = "./img/poster/"
i = 0
print(len(list(cur)))
# for poster in cur:
#     i += 1
#     # print(poster[0])
#     url = poster[0]
#     code = poster[1]
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = bs(res.text, "lxml")

    # Path(fileDir).mkdir(parents=True, exist_ok=True)
    # with open(fileDir + "/m_" + code + ".jpg", "wb") as f:
    #     f.write(res.content)
print(i)

