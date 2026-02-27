X=int(input())
NUM=[64]

while X!=64:
    n = NUM.pop()//2

    if sum(NUM) + n > X:
        NUM.append(n)
    elif sum(NUM) + n < X:
        [NUM.append(n) for _ in range(2)]
    else:
        NUM.append(n)
        break



print(len(NUM))


