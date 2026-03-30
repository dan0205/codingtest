N=int(input())

#   0  1  2  3  4
DP=[0, 1, 2, 3, 5]
for i in range(5, N+1):
    DP.append((DP[i-1]+DP[i-2])%10007)

print(DP[N])