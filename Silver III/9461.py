T=int(input())
DP=[0,1,1,1]

for i in range(4, 101):
    DP.append(DP[i-3]+DP[i-2])

for _ in range(T):
    print(DP[int(input())])