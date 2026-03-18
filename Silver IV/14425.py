N,M=map(int,input().split())
STR_A=[input() for _ in range(N)]
COT=0

for i in range(M):
    if input() in STR_A:
        COT += 1

print(COT)