N=int(input())
NUM=list(map(int, input().split()))
NUM.sort()

DP=[NUM[0]]
for i in range(1, N):
    DP.append(DP[i-1]+NUM[i])

print(sum(DP))