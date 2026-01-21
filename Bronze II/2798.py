N,M=map(int,input().split())
li = list(map(int,input().split()))
res_max=0

for i in range(N):
    num_a = li[i]
    for j in range(i+1, N):
        num_b = li[j]
        for k in range(j+1, N):
            num_c=li[k]
            
            tem_sum = num_a + num_b + num_c
            if(tem_sum <= M):
                res_max = max(res_max, tem_sum)

print(res_max)
            