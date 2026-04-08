N,M=map(int,input().split())
NUM=list(map(int, input().split()))
NUM.sort()

RES=[]
LIST=[]

def backtrack(RES):
    if len(RES)==M:
        LIST.append(RES[:])
    
    else:
        if RES:
            COPY = [n for n in NUM if n >= RES[-1]]
        else:
            COPY = NUM
        
        for n in COPY:
            RES.append(n)
            backtrack(RES)
            RES.pop()

backtrack(RES)
for line in LIST:
    print(*line)

