N, A, B = map(int,input().split())

def func(n: int):
    if n%2 == 0:
        return n//2
    else:
        return (n+1)//2

ROUND=0
while A!=B:
    A, B = func(A), func(B)
    ROUND += 1

print(ROUND)