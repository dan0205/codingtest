input_list = [input() for _ in range(8)]
res=0
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0 and input_list[i][j]=='F':
            res+=1
print(res)


