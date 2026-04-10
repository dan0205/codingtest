from collections import deque

N=int(input())
STACK_1 = deque(list(map(int,input().split())))
STACK_2 = deque()
CHECK=1
flag=True

while CHECK <= N:
    if not STACK_2:
        STACK_2.append(STACK_1.popleft())
    else:
        if STACK_2[-1] != CHECK and STACK_1:
            STACK_2.append(STACK_1.popleft())
        elif STACK_2[-1] != CHECK and not STACK_1:
            flag=False
            break
        else:
            STACK_2.pop()
            CHECK += 1
            
print('Nice' if flag else 'Sad')

