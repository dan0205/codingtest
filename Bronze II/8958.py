T=int(input())
for i in range(T):
    my_str = input()

    res_sum = 0
    res_cot = 1

    for j in range(len(my_str)):
        if my_str[j]=='O':
            res_sum += res_cot
            res_cot += 1
        else:
            res_cot = 1
    
    print(res_sum)
