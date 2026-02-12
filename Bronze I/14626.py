STR = input()
SUM = 0
flag=False

for i in range(13):
    if STR[i]!='*':
        SUM += int(STR[i]) if i%2==0 else int(STR[i])*3
    else:
        flag = True if i%2==0 else False

for i in range(10):
    RES = i if flag else i*3

    if(SUM + RES)%10 == 0:
        print(i)
        break
