import cx_Oracle
import numpy as np
import pandas as pd


def doublebubleSort(li, li2):
    list_length = len(li)
    for i in range(list_length - 1):
        for j in range(list_length - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                li2[j], li2[j + 1] = li2[j + 1], li2[j]


conn = cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
cur = conn.cursor()

sql = "SELECT * FROM MOVIE_GENRE"
cur.execute(sql)

movieFetch = [i for i in cur.fetchall()]
# userSeq = 100 번인 유저의 영화 성향을 정렬
sql = "SELECT * FROM USER_GENRE"
cur.execute(sql)

userFetch = [i for i in cur.fetchall()]

# print(movieFetch)
# print("----------------------")
# print(userFetch)

conn.close()

len_user = len(userFetch)
len_movie = len(movieFetch)


userList = list([list(u[1:10]) for u in userFetch])
print(userList)
movieList = list(list(m[1:10]) for m in movieFetch)

print(movieList)

userResSeqList = []
movieResSeqList = []
scResList = []

genreLen = 8

for i, user in enumerate(userList):
    movieScRow = []
    userSeqRow = []
    movieSeqRow = []
    for j, movie in enumerate(movieList):
        print("[", i, "][", j, "]")
        sc = 0

        print()
        for k in range(0, genreLen):
            # print(user[k])
            # print(movie[k])
            sc += user[k] * movie[k]
        print(sc)
        movieSeqRow.append(movie[genreLen])
        userSeqRow.append(user[genreLen])
        movieScRow.append(sc)
        print()
    userResSeqList.append(userSeqRow)
    movieResSeqList.append(movieSeqRow)
    scResList.append(movieScRow)
# print(movieResSeqList)

# ------------------ result ------------------
print("------------------ result ------------------")
print("------------------ scResList ------------------")
print(scResList)
print("------------------ movieResSeqList ------------------")
print(movieResSeqList)
print("------------------ userResSeqList ------------------")
print(userResSeqList)

resultDate = []
resultDate.append(movieResSeqList)
resultDate.append(userResSeqList)
resultDate.append(scResList)

#
# doublebubleSort(scResList, movieResSeqList)
#
# print(movieResSeqList)
# print(scResList)




# print(RateData)


# submovdata = pd.Series(movieList)
# subuserdata = pd.Series(userList)
#
# Len_User = subuserdata.shape[0]
# Len_Mov = submovdata.shape[0]
# Genre = 8
#
# RateData = np.zeros((Len_User, Len_Mov))
#
#
# for U in range(Len_User):
#     for M in range(Len_Mov):
#         for G in range(Genre):
#             RateData[U][M] += submovdata.values[M, G]*subuserdata.values[U, G]
#
# print(RateData)