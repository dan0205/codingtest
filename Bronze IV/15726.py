li=list(map(int,input().split()))
res=int(max(li[0]*li[1]/li[2], li[0]/li[1]*li[2]))
print(res)