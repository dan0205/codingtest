N,M=map(int,input().split())
RESULT=[] 

def backtrack(PATH):
    
    if len(PATH)==M:
        RESULT.append(PATH[:])
        return
    else:
        for i in range(1, N+1):
            PATH.append(i)
            backtrack(PATH)
            PATH.pop()

backtrack([])

for line in RESULT:
    print(*line)