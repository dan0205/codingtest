str_list = [input() for _ in range(5)]
res_list = []

max_len = 0
for i in range(5):
    max_len = max(max_len, len(str_list[i]))

for i in range(max_len):
    for j in range(5):
        if len(str_list[j]) <= i:
            continue
        res_list.append(str_list[j][i])


print(*res_list, sep='')





