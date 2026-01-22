n=int(input())
res_list=[0,1]

for i in range(2, n+1):
    res_list.append(res_list[i-1]+res_list[i-2])

print(res_list[n])