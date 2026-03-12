N=int(input())
STR = [input() for _ in range(N)]

for line in STR:

    RES=0
    for c in line:
        if c == '(':
            RES += 1
        elif c == ')' and RES != 0:
            RES -= 1
        elif c == ')' and RES == 0:
            RES = -1
            break

    
    print('YES' if RES == 0 else 'NO')

