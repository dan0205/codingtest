import sys

N=int(input())
LIST=[]
for i in range(N):
    STR=sys.stdin.readline().strip().split()
    LIST.append([STR[0], int(STR[1]), int(STR[2]), int(STR[3])])

LIST.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
print(*[LIST[i][0] for i in range(N)], sep='\n')