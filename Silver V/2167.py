N,M=map(int,input().split())
NUM=[list(map(int,input().split())) for _ in range(N)]
DP=[[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i==0 and j==0:
            DP[i][j] = NUM[i][j]
        elif i==0:
            DP[i][j] = DP[i][j-1] + NUM[i][j]
        elif j==0:
            DP[i][j] = DP[i-1][j] + NUM[i][j]
        else:
            DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + NUM[i][j]


T=int(input())
for _ in range(T):
    i,j,x,y = map(int,input().split())
    i,j,x,y = i-1,j-1,x-1,y-1
    
    if i==0 and j==0:
        print(DP[x][y])
    elif i==0:
        print(DP[x][y] - DP[x][j-1])
    elif j==0:
        print(DP[x][y] - DP[i-1][y])
    else:
        print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])
    
