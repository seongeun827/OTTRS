import cx_Oracle
import numpy as np
import pandas as pd


def doublebubleSort(li, li2):
    list_length = len(li)
    for i in range(list_length - 1):
        for j in range(list_length - 1):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                li2[j], li2[j + 1] = li2[j + 1], li2[j]

def getMovieGenreList(userSeq):
    conn = cx_Oracle.connect("scott","tigertiger","orcl.cgnlgvycsnjd.us-east-2.rds.amazonaws.com:1521/orcl")
    cur = conn.cursor()

    sql = "SELECT * FROM MOVIE_GENRE"
    cur.execute(sql)

    movieFetch = [i for i in cur.fetchall()]
    # userSeq = 100 번인 유저의 영화 성향을 정렬
    sql = "SELECT * FROM USER_GENRE WHERE USERSEQ = "+str(userSeq)
    cur.execute(sql)

    userFetch = [i for i in cur.fetchall()]

    # print(movieFetch)
    # print("----------------------")
    # print(userFetch)

    conn.close()

    len_user = len(userFetch)
    len_movie = len(movieFetch)

    # print(len_user)
    # print(len_movie)
    userList = list(userFetch[0][1:10])
    # print(userList)
    movieList = []
    for movie in movieFetch:
        movieList.append(list(movie[1:10]))
    # print(movieList)


    movieResSeqList = []
    scResList = []

    genreLen = 8
    for i, movie in enumerate(movieList):
        sc = 0
        print()
        for j in range(0, genreLen):
            sc += movie[j] * userList[j]
        movieResSeqList.append(movie[8])
        scResList.append(sc)

    # print(movieResSeqList)
    # print(scResList)

    doublebubleSort(scResList, movieResSeqList)

    # print(scResList)

    return movieResSeqList


