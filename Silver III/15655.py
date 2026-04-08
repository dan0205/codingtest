N,M = map(int, input().split())
NUM=list(map(int, input().split()))
NUM.sort()
RES=[]

def backtrack(LIST: list):
    if len(LIST)==M:
        RES.append(LIST[:])
    else:
        if LIST:
            COPY = [n for n in NUM if n > LIST[-1]]
        else:
            COPY = NUM
        
        for n in COPY:
            LIST.append(n)
            backtrack(LIST)
            LIST.pop()

backtrack([])
for line in RES:
    print(*line)
