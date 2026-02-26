T=int(input())
NUM = [list(map(int,input().split())) for _ in range(T)]

for i in range(len(NUM)):
    dnl, bot = 1, 1
    for j in range(NUM[i][0]+1, NUM[i][1]+1):
        dnl *= j
    for j in range(1, NUM[i][1]-NUM[i][0]+1):
        bot *= j

    print(dnl//bot)
