import sys
from collections import deque
input = sys.stdin.readline

N=int(input())
NUM = deque(range(1, N+1))


while len(NUM)>1:
    NUM.popleft()
    NUM.append(NUM.popleft())

print(*NUM)