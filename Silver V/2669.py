NUM=[list(map(int,input().split())) for _ in range(4)]
RES=[[0]*101 for _ in range(101)]


for i in range(4):
    for j in range(NUM[i][0], NUM[i][2]):
        for k in range(NUM[i][1], NUM[i][3]):
            RES[j][k] = 1


SUM=0
for line in RES:
    SUM += sum(line)

print(SUM)
