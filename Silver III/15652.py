N,M=map(int, input().split())
BASE=[n for n in range(1, N+1)]

def func(NUM: list):
    if M-len(NUM) == 0:
        print(*NUM)
    else:
        if not NUM:
            for n in BASE:
                func(NUM + [n])
        else:
            TMP = [n for n in BASE if n >= max(NUM)]
            for n in TMP:
                func(NUM + [n])
    
func([])