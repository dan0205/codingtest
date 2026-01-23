L=int(input())
input_string=input()
res_num=0

for i in range(L):
    idx_val = ord(input_string[i])-ord('a')+1
    res_num += idx_val * (31**i)
print(res_num%1234567891)