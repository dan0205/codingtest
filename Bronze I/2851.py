def _func(a:int, b:int) -> int:
    if abs(a-100) < abs(b-100):
        return a
    elif abs(a-100) == abs(b-100):
        return a if a>b else b
    else:
        return b


NUM = [int(input()) for _ in range(10)]
RES = 0
SUM,FIN=0,sum(NUM)

for i in range(0, len(NUM)):
    SUM += NUM[i]
    if SUM > 100:
        FIN = _func(SUM, SUM-NUM[i])
        break
    
RES = _func(RES, FIN)
print(RES)
     