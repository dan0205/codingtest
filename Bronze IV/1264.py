target = {'a','e','i','o','u','A','E','I','O','U'}

while True:
    str = input()
    sum = 0

    if(str == '#'):
        break;

    for i in str:
        if i in target:
            sum += 1

    print(sum)
