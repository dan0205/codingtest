str = input()
res = 0

for i in range(len(str)):
    if(i!=len(str)-1 and str[i+1]!='0'):
        res += int(str[i])
    elif(i!=len(str)-1 and str[i+1]=='0'):
        res += int(str[i:i+2])
        i+=1
    else:
        res += int(str[i])

print(res)