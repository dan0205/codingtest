str = input()

array = [0]*26
for i in range(len(str)):
    array[ord(str[i])-ord('a')] += 1


print(*(f"{array[i]}" for i in range (len(array))))