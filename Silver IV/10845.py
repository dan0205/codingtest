from collections import deque
import sys

input=sys.stdin.readline

N=int(input())
DEQUE = deque()

for _ in range(N):
    STR = input().split()

    if STR[0] == 'push':
        DEQUE.append(STR[1])
    elif STR[0] == 'pop':
        print(-1 if not DEQUE else DEQUE.popleft())
    elif STR[0] == 'size':
        print(len(DEQUE))
    elif STR[0] == 'empty':
        print(1 if not DEQUE else 0)
    elif STR[0] == 'front':
        print(-1 if not DEQUE else DEQUE[0])
    elif STR[0] == 'back':
        print(-1 if not DEQUE else DEQUE[-1])


