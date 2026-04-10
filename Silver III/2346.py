from collections import deque

N=int(input())
DEQ=deque(range(1, N+1))
NUM=list(map(int, input().split()))


# 1 2 3  4  5
# 3 2 1 -3 -1


# 1 2 3 4 5 -> 1

# 2 3 4 5

# 3 4 5 2

# 4 5 2 3 -> 4

# 5 2 3

# 3 5 2

# 2 3 5 

# 5 2 3 -> 5

# 2 3

# 3 2 -> 3


DICT = {}
for i in range(1, N+1):
    DICT[i] = NUM[i-1]



def RIGHT(CHECK: int):
    for _ in range(CHECK-1):
        DEQ.append(DEQ.popleft())

def LEFT(CHECK: int):
    CHECK = -CHECK
    for _ in range(CHECK):
        DEQ.appendleft(DEQ.pop())



RES=[1]
CHECK=DICT[DEQ.popleft()]
while DEQ:
    if CHECK>0:
        RIGHT(CHECK)
        i = DEQ.popleft()
        RES.append(i)
        CHECK = DICT[i]
    else:
        LEFT(CHECK)
        i = DEQ.popleft()
        RES.append(i)
        CHECK = DICT[i]

print(*RES)