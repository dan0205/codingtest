N=int(input())
std_num = list(map(int,input().split()))
std_list = [i for i in range(1, N+1)]


for i in range(len(std_num)):
    ticket = std_num[i]
    std_list[i-ticket], std_list[i-ticket+1:i+1] = std_list[i], std_list[i-ticket:i]

print(*std_list)
