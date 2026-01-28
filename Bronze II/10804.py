num_list = [i for i in range(1, 21)]

for i in range(10):
    start_idx, end_idx = map(int,input().split())
    num_list[start_idx-1:end_idx] = num_list[start_idx-1:end_idx][::-1]

print(*num_list)
