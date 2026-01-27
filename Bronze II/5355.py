T=int(input())
for i in range(T):
    str_i = list(input().split())
    base_num = float(str_i[0])

    for j in range(1, len(str_i)):
        if str_i[j]=='@':
            base_num *= 3
        elif str_i[j]=='%':
            base_num += 5
        elif str_i[j]=='#':
            base_num -= 7
    
    print(f"{base_num:.2f}")