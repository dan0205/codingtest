M=int(input())
N=int(input())
res_sum=0
res_min=10000

for i in range(M, N+1):
    if (i**0.5)%1==0:
        res_sum += i
        res_min = min(res_min, i)

if(res_sum == 0):
    print(-1)
else:
    print(res_sum, res_min, sep='\n')