while True:
    str = input()
    if (str=='END'): break

    for i in range(len(str)):
        print(str[len(str)-1-i],end='')

    print('')