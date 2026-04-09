N=int(input())

NUM=[n for n in range(1, N+1)]
RES=[]

def backtrack(LIST: list):
    if len(LIST)==N:
        RES.append(LIST[:])
    else:
        COPY = [n for n in NUM if n not in LIST]
        for n in COPY:
            LIST.append(n)
            backtrack(LIST)
            LIST.pop()

backtrack([])
for line in RES:
    print(*line)