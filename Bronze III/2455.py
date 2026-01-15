res=[]
for i in range(4):
    a,b=map(int,input().split())
    if(i==0):
        res.append(b)
    else:
        res.append(res[i-1]-a+b)

print(max(res))