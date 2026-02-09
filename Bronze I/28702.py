def _func(RES: int) -> str:
    if RES%3==0 and RES%5==0:
        return 'FizzBuzz'
    elif RES%3==0:
        return 'Fizz'
    elif RES%5==0:
        return 'Buzz'
    else:
        return str(RES)

STR = [input() for _ in range(3)]
idx=0

for i in range(3):
    if STR[i]!='Fizz' and STR[i]!='Buzz' and STR[i]!='FizzBuzz':
        idx = i

RES = int(STR[idx]) + (3-idx)
print(_func(RES))
