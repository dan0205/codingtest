N=int(input())

DP = [[0,1], [1,1]]
for i in range(2, N):
    A = DP[i-1][1]
    B = DP[i-1][0] + DP[i-1][1]
    DP.append([A,B])

print(*DP[N-1])
