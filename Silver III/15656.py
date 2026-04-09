N,M=map(int,input().split())
NUM=list(map(int, input().split()))
NUM.sort()

RES=[]
def backtrack(LIST: list):
    if len(LIST)==M:
        RES.append(LIST[:])
    else:
        for n in NUM:
            LIST.append(n)
            backtrack(LIST)
            LIST.pop()
    
backtrack([])
for line in RES:
    print(*line)
