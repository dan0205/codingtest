def my_func(new_N: int) -> int:
    base_10  = str(new_N%10)
    
    if len(str(new_N))==1:
        base_1 = str(new_N)
    else:
        base_1 = str((int(str(new_N)[0]) + int(str(new_N)[1])) % 10)

    return int(base_10 + base_1)


N=int(input())
new_N = my_func(N)
count = 1

while N!=new_N:
    new_N = my_func(new_N)
    count += 1

print(count)

