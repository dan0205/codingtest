N=int(input())
min_x, max_x, min_y, max_y = 0,0,0,0

for i in range(N):
    x,y=map(int,input().split())
    if(i==0):
        min_x,max_x,min_y,max_y = x,x,y,y
    else:
        min_x=min(x,min_x)
        max_x=max(x,max_x)
        min_y=min(y,min_y)
        max_y=max(y,max_y)

print((max_x-min_x) * (max_y-min_y))
