N,M=map(int, input().split())
num_list = [i for i in range(1, N+1)]

for i in range(M):
    a,b=map(int,input().split())
    num_list[a-1], num_list[b-1] = num_list[b-1], num_list[a-1]

print(*num_list)