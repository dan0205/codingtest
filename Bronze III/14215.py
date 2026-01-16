length_list = list(map(int,input().split()))

while True:
    if sum(length_list) <= 2 * max(length_list):
        length_list[length_list.index(max(length_list))] -= 1
    else:
        break

print(sum(length_list))