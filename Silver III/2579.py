N=int(input())

NUM=[0] + [int(input()) for _ in range(N)]
DP=[0]

if N==1:
    print(NUM[1])
elif N==2:
    print(NUM[1]+NUM[2])
else:
    DP.append(NUM[1])
    DP.append(NUM[1]+NUM[2])

    for i in range(3, N+1):
        DP.append(max(DP[i-3]+NUM[i-1]+NUM[i], DP[i-2]+NUM[i]))

    print(DP[N])