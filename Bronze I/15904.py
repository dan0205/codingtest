def _func(STR: list, CHR: str, idx: int) -> int:

    for i in range(idx, len(STR)):
        if STR[i] == CHR:
            return i

    return -1

STR = input()
UCPC = ['U', 'C', 'P', 'C']
idx = 0
flag = False

for chr in UCPC:
    idx = _func(STR, chr, idx)
    if idx == -1:
        flag = True
        break

print("I hate UCPC" if flag else "I love UCPC")

