from collections import deque
import sys

input = sys.stdin.readline
DEQ=deque()

N=int(input())
for i in range(N):
    STR=input().split()
    
    if STR[0] == 'push_front':
        DEQ.appendleft(int(STR[1]))
    elif STR[0] == 'push_back':
        DEQ.append(int(STR[1]))        
    elif STR[0] == 'pop_front':
        print(-1 if not DEQ else DEQ.popleft())        
    elif STR[0] == 'pop_back':
        print(-1 if not DEQ else DEQ.pop())        
    elif STR[0] == 'size':
        print(len(DEQ))
    elif STR[0] == 'empty':
        print(1 if not DEQ else 0)        
    elif STR[0] == 'front':
        print(-1 if not DEQ else DEQ[0])        
    elif STR[0] == 'back':
        print(-1 if not DEQ else DEQ[-1])        