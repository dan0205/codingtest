N=int(input())
LIST = [input().split() for _ in range(N)]

for i in range(N):
    LIST[i][0], LIST[i][1], LIST[i][2], LIST[i][3] = \
        int(LIST[i][3]), int(LIST[i][2]), int(LIST[i][1]), LIST[i][0]

LIST.sort()
print(LIST[N-1][3])
print(LIST[0][3])