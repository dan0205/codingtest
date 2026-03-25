import sys

def Find(n: int):
    if n==0 or n==1:
        return 2
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return -1
    return n

T=int(input())
for i in range(T):
    n=int(sys.stdin.readline())
    RES=0
    while True:
        TMP = Find(n)
        if TMP == -1:
            n += 1
        else:
            RES = TMP
            break
    
    print(RES)