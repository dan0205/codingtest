import sys
N,K=map(int, sys.stdin.readline().strip().split())
NUM=list(map(int,sys.stdin.readline().strip().split()))
MAX=[]

SUM=sum(NUM[0:K])
MAX.append(SUM)
# 10,2 -> 0,1   1,2     2,3     
for i in range(K, N):
    # 10, 2 라면 (0,8) -> 0,1,2,,,7 -> 근데 마지막 (8,9)도 체크해야됌
    SUM += NUM[i]
    SUM -= NUM[i-K]
    MAX.append(SUM)

print(max(MAX))