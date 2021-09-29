import cx_Oracle

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

testMovie = Movie()
testMovie.MOVIETITLE = '너의 이름은.'
testMovie.MOVIECODE = '2909332'
testMovie.MOVIEPLOT = '''
아직 만난 적 없는 너를, 찾고 있어

천년 만에 다가오는 혜성
기적이 시작된다

도쿄에 사는 소년 ‘타키’와 시골에 사는 소녀 ‘미츠하’는
서로의 몸이 뒤바뀌는 신기한 꿈을 꾼다
낯선 가족, 낯선 친구들, 낯선 풍경들...
반복되는 꿈과 흘러가는 시간 속, 마침내 깨닫는다
우리, 서로 뒤바뀐 거야?

절대 만날 리 없는 두 사람
반드시 만나야 하는 운명이 되다

서로에게 남긴 메모를 확인하며
점점 친구가 되어가는 ‘타키’와 ‘미츠하’
언제부턴가 더 이상 몸이 바뀌지 않자
자신들이 특별하게 이어져있었음을 깨달은
‘타키’는 ‘미츠하’를 만나러 가는데...

잊고 싶지 않은 사람
잊으면 안 되는 사람
너의 이름은?
'''
testMovie.MOVIEMODE = '구매'
testMovie.MOVIEPRICE = '1,200'
testMovie.MOVIEPOSTERIMG = 'https://movie-phinf.pstatic.net/20171222_70/1513920001726sikUX_JPEG/movie_image.jpg?type=f172_234'
testMovie.MOVIEDIRECTOR = '신카이 마코토'
testMovie.MOVIEGENRE = '애니메이션'


def getConn():
    # conn = cx_Oracle.connect("scott", "scott1234!", "orcl.cu1tbymhc2wb.ap-northeast-2.rds.amazonaws.com:1521/orcl")
    return cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")


if __name__ == "__main__":
    conn =getConn()
    # print(conn)
    cur = conn.cursor()

    # sql = """
    #     INSERT INTO MOVIE VALUES (MOVIE_SEQ.NEXTVAL,
    #      :MOVIETITLE,
    #       :MOVIECODE,
    #       :MOVIEPLOT,
    #       :MOVIEMODE,
    #       :MOVIEPRICE,
    #       :MOVIEPOSTERIMG,
    #       :MOVIEDIRECTOR,
    #       :MOVIEGENRE)
    # """
    #
    # cur.execute(sql, MOVIETITLE=testMovie.MOVIETITLE,
    #             MOVIECODE=testMovie.MOVIECODE,
    #             MOVIEPLOT=testMovie.MOVIEPLOT,
    #             MOVIEMODE=testMovie.MOVIEMODE,
    #             MOVIEPRICE=testMovie.MOVIEPRICE,
    #             MOVIEPOSTERIMG=testMovie.MOVIEPOSTERIMG,
    #             MOVIEDIRECTOR=testMovie.MOVIEDIRECTOR,
    #             MOVIEGENRE=testMovie.MOVIEGENRE
    #             )
    print("-------------------------")
    sql = """ 
    
    INSERT INTO MOVIE
    VALUES (MOVIE_SEQ.NEXTVAL,
    """
    sql += "'"+testMovie.MOVIETITLE+"',"
    sql += "'"+testMovie.MOVIECODE+"',"
    sql += "'"+testMovie.MOVIEPLOT+"',"
    sql += "'"+testMovie.MOVIEMODE+"',"
    sql += "'"+testMovie.MOVIEPRICE+"',"
    sql += "'"+testMovie.MOVIEPOSTERIMG+"',"
    sql += "'"+testMovie.MOVIEDIRECTOR+"',"
    sql += "'"+testMovie.MOVIEGENRE+"'"
    sql += ")"
    print(sql)
    print("-------------------------")
    # print("test :", testMovie.MOVIEPOSTERIMG)

    cur.execute(sql)
    conn.commit()

    sql ="SELECT max(MOVIESEQ) from MOVIE"
    cur.execute(sql)

    # print(cur[0])

    lastId = 0
    for d in cur:
        lastId = d[0]





    # conn.close()


"""
Name : @aws


Host : orcl.cu1tbymhc2wb.ap-northeast-2.rds.amazonaws.com
SID : orcl
User : scott
Password : scottt1234!

URL : jdbc:oracle:thin:@orcl.cu1tbymhc2wb.ap-northeast-2.rds.amazonaws.com:1521:orcl
"""