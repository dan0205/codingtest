T=int(input())
NUM=[list(map(int,input().split())) for _ in range(T)]

RES=[[0]*100 for _ in range(100)]

for x, y in NUM:
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            RES[i][j]=1

print(sum(line.count(1) for line in RES))
