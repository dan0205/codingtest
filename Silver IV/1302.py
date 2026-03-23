N=int(input())
DICT={}

for i in range(N):
    BOOK = input()
    if BOOK in DICT:
        DICT[BOOK] += 1
    else:
        DICT[BOOK] = 1

RES=sorted(DICT.items(), key=lambda x: (-x[1], x[0]))

print(RES[0][0])