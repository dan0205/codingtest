from collections import deque
import sys

N=int(input())
RES=0

def func(STR: str) -> int:
    DEQ=deque()
    DEQ.append(STR[0])

    for i in range(1, len(STR)):
        if not DEQ:
            DEQ.append(STR[i])
        elif DEQ[-1] == STR[i]:
            DEQ.pop()
        else:
            DEQ.append(STR[i])
    
    return 0 if DEQ else 1

for i in range(N):
    STR = sys.stdin.readline().strip()
    RES += func(STR)

print(RES)