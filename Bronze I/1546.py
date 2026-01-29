N=int(input())
num_list = list(map(int, input().split()))
M=max(num_list)
res_sum=0

for num in num_list:
    res_sum += (num/M)*100

print(res_sum/N)
