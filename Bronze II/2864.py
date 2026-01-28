num_a, num_b = input().split()

max_a, max_b = num_a.replace('5','6'), num_b.replace('5','6')
min_a, min_b = num_a.replace('6','5'), num_b.replace('6','5')

print(int(min_a)+int(min_b), int(max_a)+int(max_b))