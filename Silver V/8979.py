N,K=map(int,input().split())
NUM=[list(map(int, input().split())) for _ in range(N)]
idx=0
for i in range(N):
    if NUM[i][0] == K:
        idx=i
        break
RES=1
for i in range(N):
    if NUM[i][1:] > NUM[idx][1:]:
        RES+=1

print(RES)