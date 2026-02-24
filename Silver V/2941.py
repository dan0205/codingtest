STR=input()
SET = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
RES=0

while len(STR)!=0:
    flag='a'

    for CHR in SET:
        if STR.startswith(CHR):
            flag=CHR
            break
    
    RES += 1
    STR = STR[len(flag):]


print(RES)
