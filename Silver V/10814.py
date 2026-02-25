T=int(input())
LIST=[input().split() for _ in range(T)]

for i in range(len(LIST)):
    LIST[i][0] = int(LIST[i][0])

LIST.sort(key=lambda x: (x[0]))

for line in LIST:
    print(*line)