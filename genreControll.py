import cx_Oracle
from random import randint

conn = cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
cur = conn.cursor()

#
# for i in range(1, 61):
#
#
#     sql = "INSERT INTO OTTRS_USER VALUES (OTTRS_USER_SEQ.nextval,'USER"+str(i)+"@test.com','abcd1234')"
#     print(sql)
#     cur.execute(sql)

#
# sql = "SELECT USERSEQ FROM OTTRS_USER"
# cur.execute(sql)
# userFetch = [i for i in cur.fetchall()]
# userSeqList = [u[0] for u in userFetch]
#
#
# print(userSeqList)
# numVal = []
# for i in range(10):
#     numVal.append(randint(0, 3))
#
# for userSeq in userSeqList:
#     sql = "INSERT INTO USER_GENRE VALUES (OTTRS_USER_SEQ.nextval," + str(numVal[0]) + ","\
#           + str(numVal[1]) + ","\
#           + str(numVal[2])+ ","\
#           + str(numVal[3])+ ","\
#           + str(numVal[4])+ ","\
#           + str(numVal[5])+ ","\
#           + str(numVal[6])+ ","\
#           + str(numVal[7])+ ","\
#           + str(numVal[8])+ ","\
#           + str(numVal[9])+ ","+str(userSeq)+")"
#     cur.execute(sql)
# for u in userSeqList:
#     print(u)

sql = "SELECT MOVIESEQ, MOVIEGENRE FROM MOVIE"
cur.execute(sql)
movieFetch = [i for i in cur.fetchall()]
movieSeqList = [u[0] for u in movieFetch]
movieGenreList = [u[1] for u in movieFetch]
print(movieSeqList)
print(movieGenreList)

for i, movieSeq in enumerate(movieSeqList):
    genre = movieGenreList[i]
    numVal = []
    for i in range(0, 8):
        numVal.append(randint(0, 7))
    if genre == '액션':
        numVal[0] = 10
    elif genre == '코미디':
        numVal[1] = 10
    elif genre == '드라마':
        numVal[2] = 10
    elif genre == '멜로':
        numVal[3] = 10
    elif genre == '공포/스릴러':
        numVal[4] = 10
    elif genre == 'SF/판타지':
        numVal[5] = 10
    elif genre == '애니메이션':
        numVal[6] = 10
    elif genre == '다큐멘터리':
        numVal[7] = 10

    sql = "INSERT INTO MOVIE_GENRE VALUES (OTTRS_USER_SEQ.nextval," + str(numVal[0]) + ","+ str(numVal[1]) + "," + str(numVal[2]) + "," + str(numVal[3]) + ","+ str(numVal[4]) + "," + str(numVal[5]) + "," + str(numVal[6]) + "," + str(numVal[7]) + "," + str(movieSeq)+")"

    print(sql)
    cur.execute(sql)

conn.commit()
conn.close()
