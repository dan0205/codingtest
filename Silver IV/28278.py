import sys
from collections import deque


N=int(input())
DEQ=deque()
for i in range(N):
    COM=sys.stdin.readline().strip().split()

    if COM[0] == '1':
        DEQ.append(int(COM[1]))
    elif COM[0] == '2':
        print(DEQ.pop() if DEQ else -1)
    elif COM[0] == '3':
        print(len(DEQ))
    elif COM[0] == '4':
        print(0 if DEQ else 1)
    elif COM[0] == '5':
        print(DEQ[-1] if DEQ else -1)