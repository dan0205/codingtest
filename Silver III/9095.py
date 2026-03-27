import sys

T=int(sys.stdin.readline())
NUM=[int(sys.stdin.readline()) for _ in range(T)]

#   0  1  2  3  4
DP=[0, 1, 2, 4, 7]
for i in range(5, 11):
    DP.append(DP[i-1]+DP[i-2]+DP[i-3])

for num in NUM:
    print(DP[num])
