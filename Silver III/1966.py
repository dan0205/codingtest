from collections import deque

def func(M, LIST):
    BASE=deque(sorted(LIST, reverse=True))
    DEQ=deque((number, idx) for idx, number in enumerate(LIST))
    COUNT=1
    
    while True:
        if DEQ[0][0]<BASE[0]:
            DEQ.append(DEQ.popleft())
        else:
            if DEQ[0][1] != M:
                DEQ.popleft()
                BASE.popleft()
                COUNT += 1
            else:
                return COUNT


T=int(input())
for _ in range(T):
    N, M = map(int, input().split())
    LIST = list(map(int, input().split()))
    print(func(M, LIST))