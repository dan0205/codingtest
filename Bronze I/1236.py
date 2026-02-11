
N,M=map(int,input().split())

INP = [input() for _ in range(N)]
res_y, res_x = 0, 0

for i in range(N):
    flag = False
    for j in range(M):
        if INP[i][j]=='X':
            flag = True
            break
    if flag == False:
        res_y += 1

for i in range(M):
    flag = False
    for j in range(N):
        if INP[j][i] == 'X':
            flag=True
            break
    if flag==False:
        res_x += 1

MIN = min(res_x, res_y)
print(MIN + abs(res_y-res_x))