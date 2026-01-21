my_str = input()

dial_list = ['ABC', 'DEF', 'GHI','JKL','MNO','PQRS','TUV','WXYZ']
res_sum=0

for dial in dial_list:
    for str_idx in my_str:
        if str_idx in dial:
            res_sum += dial_list.index(dial) + 3

print(res_sum)