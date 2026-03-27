import sys
T=int(input())

# 0, 1      1       2     3      4   
DP=[[1,0], [0,1], [1,1], [1,2], [2,3]]

for i in range(5, 41):
    RES_0 = DP[i-1][0] + DP[i-2][0]
    RES_1 = DP[i-1][1] + DP[i-2][1]
    DP.append([RES_0, RES_1])

for i in range(T):
    n = int(sys.stdin.readline())
    print(*DP[n])