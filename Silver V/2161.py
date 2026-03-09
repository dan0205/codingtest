N=int(input())
RES=[]
NUM=[i for i in range(1, N+1)]

while NUM:
    RES.append(NUM.pop(0))
    if NUM:
        NUM.append(NUM.pop(0))

print(*RES)