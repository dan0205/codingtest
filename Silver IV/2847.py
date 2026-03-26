N=int(input())
NUM=[int(input()) for _ in range(N)]


BASE=NUM[-1]
COUNT=0
for i in range(1, N):
    if NUM[N-i-1]>=BASE:
        COUNT+=(NUM[N-i-1]-BASE+1)
        BASE -= 1
    else:
        BASE = NUM[N-i-1]

print(COUNT)