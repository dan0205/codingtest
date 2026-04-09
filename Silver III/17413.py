from collections import deque

DEQ=deque()
STR=input() + ' '
flag=False

# abc -> cba
# abc abc -> cba cba


for char in STR:
    DEQ.append(char)

    if char==' ' and not flag:
        DEQ.pop()
        print(*reversed(DEQ),sep='',end='')
        DEQ.clear()
        print(' ',end='')

    if char=='<':
        DEQ.pop()
        print(*reversed(DEQ),sep='',end='')
        DEQ.clear()
        DEQ.append('<')
        flag = True
    
    if char=='>':
        print(*DEQ,sep='',end='')
        DEQ.clear()
        flag=False