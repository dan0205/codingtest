column = 0
row = 0
max_num = 0

for i in range(1, 10):
    li = list(map(int,input().split()))
    if(max(li)>=max_num):
        max_num = max(max_num, max(li))
        column = i
        row = li.index(max(li)) + 1

print(max_num)
print(column, row)

