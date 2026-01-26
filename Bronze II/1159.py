N=int(input())

res_list = [0] * (ord('z') - ord('a') + 1)

for i in range(N):
    name = input()
    res_list[ord(name[0]) - ord('a')] += 1

flag = False
for idx in range(len(res_list)):
    if(res_list[idx]>=5):
        flag = True
        print(chr(ord('a') + idx), end='')
    
if flag==False:
    print("PREDAJA")


