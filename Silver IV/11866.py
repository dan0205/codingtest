from collections import deque

N,K=map(int, input().split())
DEQ = deque(range(1, N+1))
print('<', end='')

count=1
while DEQ:
    if count == K:
        print(DEQ.popleft(), end='')
        if DEQ:
            print(end=', ')

        count=1
    else:
        DEQ.append(DEQ.popleft())
        count += 1

print('>')

