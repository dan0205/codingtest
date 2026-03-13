N,K=map(int,input().split())
NUM=[int(input()) for _ in range(N)]


COUNT=0
NUM.sort(reverse=True)

for i in range(N):
    if K >= NUM[i]:
        DIV, MOD = divmod(K, NUM[i])
        COUNT += DIV
        K = MOD

print(COUNT)