N,K=map(int,input().split())
NUM=[i for i in range(2, N+1)]

COUNT=0
RES=0
while RES==0:
    MIN = NUM[0]
    for i in range(MIN, N+1, MIN):
        
        if i in NUM:
            NUM.remove(i)
            COUNT += 1

        if COUNT == K:
            RES=i
            break

print(RES)
