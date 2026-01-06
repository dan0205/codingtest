li=[]

for i in range(6):
    li.append(int(input()))

total = sum(sorted(li[:4], reverse=True)[:3]) + max(li[4:6])

print(total)

