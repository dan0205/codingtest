import sys

N=int(input())

def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

if N==0:
    print(0)
else:

    NUM=[int(sys.stdin.readline().strip()) for _ in range(N)]
    NUM.sort()

    CHK=round(N * 0.15)
    NUM = NUM[CHK:(N-CHK)]

    print(round(sum(NUM)/len(NUM)))
