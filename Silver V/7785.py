T=int(input())
my_map = dict()

for i in range(T):
    name, state = input().split()
    if state == 'enter':
        my_map[f'{name}'] = 1
    else:
        del my_map[f'{name}']

result = sorted(my_map.keys(), reverse=True)
print(*result, sep='\n')
