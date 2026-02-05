def _func(CHAR: str) -> str:
    val = ord(CHAR)
    if ord('z') >= val and val >= ord('a'):
        return chr((((val - ord('a')) + 13) % (ord('z')-ord('a')+1)) + ord('a'))
    elif ord('Z') >= val and val >= ord('A'):
        return chr((((val - ord('A')) + 13) % (ord('Z')-ord('A')+1)) + ord('A'))
    else:
        return CHAR




STR = input()

for i in range(len(STR)):
    print(_func(STR[i]), end='')
    