M,N=[int(input()) for _ in range(2)]
res_sum=0
res_min=10001

for i in range(M, N+1):
    flag=True

    if i == 1:
        flag=False
    elif i != 2:
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                flag=False
                break

    if flag:
        res_sum += i
        res_min = min(res_min, i)

if res_min==10001:
    print("-1")
else:
    print(res_sum, res_min, sep='\n')