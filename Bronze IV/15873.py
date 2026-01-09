str = input()
res = 0
skip = False

for i in range(len(str)):
    if skip:
        skip=False
        continue
    
    if i+1<len(str) and str[i+1] == '0':
        res += int(str[i:i+2])
        skip=True

    else:
        res += int(str[i])

print(res)