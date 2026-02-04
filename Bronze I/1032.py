N=int(input())
STR_list = [input() for _ in range(N)]
RES = []

for i in range(len(STR_list[0])):
    CHAR = STR_list[0][i]
    flag = True
    for j in range(1, N):
        if CHAR != STR_list[j][i]:
            flag = False
            break
    if flag:
        RES.append(CHAR)
    else:
        RES.append('?')

print(*RES, sep='')