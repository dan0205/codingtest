N,M=map(int,input().split())

BASE = [n for n in range(1, N+1)]

def func(NUM: list):
    if M - len(NUM) == 0:
        print(*NUM)
        return NUM
    else:
        NOT = [n for n in BASE if n not in NUM]
        for n in NOT:
            func(NUM + [n])

func([])
