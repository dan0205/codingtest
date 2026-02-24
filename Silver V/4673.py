def _func(i: int) -> int:
    RES = i

    while i > 0:
        RES += i % 10
        i = i // 10

    return RES

NUM=[0]*10001

for i in range(1, 10001):
    if _func(i) > 10000:
        continue
    NUM[_func(i)] = 1


for i in range(1, len(NUM)):
    if NUM[i] == 0:
        print(i)