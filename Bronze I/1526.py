N=int(input())

for i in range(N, 3, -1):
    STR = str(i)
    flag = True
    for CHR in STR:
        if CHR != '4' and CHR != '7':
            flag = False
            break
    
    if flag:
        print(i)
        break