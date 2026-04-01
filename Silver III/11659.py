import sys

N,M=map(int, input().split())
NUM=list(map(int, sys.stdin.readline().strip().split()))
DP=[0]
for i in range(N):
    DP.append(NUM[i]+DP[i])

for _ in range(M):
    A,B = map(int, sys.stdin.readline().strip().split())
    print(DP[B]-DP[A-1])
