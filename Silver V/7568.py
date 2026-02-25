T=int(input())
NUM=[list(map(int,input().split())) for _ in range(T)]

for i in range(T):
    rank = 1
    for j in range(T):
        if NUM[j][0] > NUM[i][0] and NUM[j][1] > NUM[i][1]:
            rank+=1
    print(rank, end=' ')