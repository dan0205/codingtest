N=int(input())
#   0  1  2  3  4  5
DP=[0, 0, 1, 1, 2, 3]

for i in range(6, N+1):
    MIN1, MIN2, MIN3 = 100000,100000,100000
    MIN1 = DP[i-1] + 1
    if i%3 == 0:
        MIN2 = DP[i//3] + 1
    if i%2 == 0:
        MIN3 = DP[i//2] + 1
    
    DP.append(min(MIN1, MIN2, MIN3))

print(DP[N])
    