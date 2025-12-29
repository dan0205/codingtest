""" a = input()
list = list(a)


for i in range(len(a)):
    if(list[i].isupper()):
        list[i] = list[i].lower()
    else:
        list[i] = list[i].upper()

a = ''.join(list)
print(a) """

a = input()
print(a.swapcase())