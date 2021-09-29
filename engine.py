import pandas as pd
import numpy as np

# 영화 데이터를 불러옴
movdata = pd.read_csv(r'.\movdata.csv')
# 영화데이터를 새로운 서브 변수에 넣어줌
submovdata = movdata
# 서브영화 데이터의 code와 title 칼럼 삭제
submovdata.drop(['code','title'], axis = 1,inplace=True)

# submovdata

# 영화 데이터를 불러옴, Index Column(Unnamed : 0) 지워줌
userdata = pd.read_csv(r'.\userdata.csv', index_col=[0])
# 영화데이터를 새로운 서브 변수에 넣어줌
subuserdata = userdata
# subuserdata

print(submovdata)
print(subuserdata)

Len_User = subuserdata.shape[0]
Len_Mov = submovdata.shape[0]
Genre = 10

RateData = np.zeros((Len_User,Len_Mov))


for U in range(Len_User):
    for M in range(Len_Mov):
        for G in range(Genre):
            RateData[U][M] += submovdata.values[M,G]*subuserdata.values[U,G]

print(RateData)