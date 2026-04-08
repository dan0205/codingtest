from collections import deque

N,M=map(int,input().split())
DEQ=deque(range(1,N+1))
NUM=list(map(int,input().split()))
RES=0

while NUM:
    target = NUM[0]
    idx = DEQ.index(target)

    if idx==0:
        DEQ.popleft()
        NUM.pop(0)

    else:
        if idx <= len(DEQ)//2:
            DEQ.rotate(-1)
        else:
            DEQ.rotate(1)
        RES += 1

print(RES)

# DEQ를 회전시키는건 rotate. DEQ의 인덱스는 index로 알면
# BASE를 사용하지 않고도 편하게 할수있네