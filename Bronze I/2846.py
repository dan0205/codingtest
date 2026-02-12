N=int(input())
NUM=list(map(int,input().split()))

MAX = 0
RES = 0

for i in range(1, N):
    if NUM[i-1] < NUM[i]:
        MAX += NUM[i]-NUM[i-1]
    else: #내리막길, 평지
        RES = max(RES, MAX)
        MAX = 0

RES = max(RES,MAX)
print(RES)
