N,M=map(int,input().split())
BASE=list(map(int,input().split()))
BASE.sort()
NUM=[]
RESULT=[]

def backtrack(NUM: list):
    if len(NUM)==M:
        RESULT.append(NUM[:])
    else:
        COPY=[i for i in BASE if i not in NUM]
        for i in COPY:
            NUM.append(i)
            backtrack(NUM)
            NUM.pop()

backtrack(NUM)
for line in RESULT:
    print(*line)