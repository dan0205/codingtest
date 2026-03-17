from collections import deque

N,K=map(int,input().split())
DEQ=deque(range(1, N+1))
NUM=[]

cot=1
while len(DEQ)>0:
    if cot == K:
        cot = 1
        NUM.append(DEQ.popleft())
    else:
        cot += 1
        DEQ.append(DEQ.popleft())


print('<', end='')
print(*NUM, sep = ', ', end='')
print('>')



