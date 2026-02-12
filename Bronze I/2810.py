N=int(input())
STR = input()

idx=0
res=0
flag=False

while idx < len(STR):
    if STR[idx]=='S':
        idx += 1
    
    else:
        if flag:
            idx += 2
            res += 1
        else:
            flag = True
            idx += 2

print(N-res)
