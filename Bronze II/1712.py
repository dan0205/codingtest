num_list = list(map(int,input().split()))
if num_list[1]>=num_list[2]:
    print(-1)
else:
    print(int(num_list[0]/(num_list[2]-num_list[1]))+1)