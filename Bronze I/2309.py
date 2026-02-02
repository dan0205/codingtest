num_list = [int(input()) for _ in range(9)]
num_list.sort()

for i in range(9):
    for j in range(i+1, 9):
        val_i, val_j = num_list[i], num_list[j]
        if sum(num_list) - val_i - val_j == 100:
            for k in range(9):
                if k==i or k==j:
                    continue
                print(num_list[k])
            exit()