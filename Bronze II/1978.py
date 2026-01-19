N=int(input())
num_list = list(map(int,input().split()))
res_sum=0
for num in num_list:
    
    bool = True
    #1은 소수가 아니니까 패스
    if num < 2:
        bool = False
    #n이 소수인지 확인 -> n보다 작은 수로 나누어지면 안된다 -> sqrt(n)보다 작은 수로 나누어지지 않으면 똑같이 소수
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            bool = False
            break
    
    if bool:
        res_sum += 1

print(res_sum)