from collections import deque
import sys
N=int(input())
DEQ=deque()

for i in range(N):
    STR=sys.stdin.readline().strip().split()
    
    if STR[0] == 'push':
        DEQ.append(int(STR[1]))
    elif STR[0] == 'pop':
        print(DEQ.popleft() if DEQ else -1)
    elif STR[0] == 'size':
        print(len(DEQ))
    elif STR[0] == 'empty':
        print(0 if DEQ else 1)
    elif STR[0] == 'front':
        print(DEQ[0] if DEQ else -1)
    elif STR[0] == 'back':
        print(DEQ[-1] if DEQ else -1)