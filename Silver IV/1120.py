A,B=input().split()

def FUNC(A:str, B:str) -> int:
    RES=0
    for i in range(len(A)):
        if A[i] != B[i]:
            RES += 1
    return RES

RES=50
for i in range(0, len(B)-len(A)+1):
    RES = min(RES, FUNC(A,B[i:i+len(A)]))
print(RES)