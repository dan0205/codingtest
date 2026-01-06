li=[]
for i in range(5):
    li.append(int(input()))

res=0

if(li[0]<0):
    res += li[2]*abs(li[0]) + li[3] + li[4]*li[1]
else:
    res += li[4]*(li[1]-li[0])

print(res)
