N=int(input())
NUM=[int(input()) for _ in range(N)]
NUM.sort(reverse=True)

MAX = 0
for i in range(N):
    MAX = max(MAX, (i+1)*NUM[i])

print(MAX)