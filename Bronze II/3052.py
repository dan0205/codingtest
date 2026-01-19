my_set = set()
num_list = list(int(input()) for _ in range(10))

for num in num_list:
    my_set.add(num%42)

print(len(my_set))