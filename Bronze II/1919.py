str_1, str_2 = list(input()), list(input())

idx=0
while idx < len(str_1):
    chr_1=str_1[idx]
    if chr_1 in str_2:
        str_1.pop(idx)
        str_2.remove(chr_1)
    else:
        idx+=1

print(len(str_1) + len(str_2))