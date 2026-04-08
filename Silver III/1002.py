def triangle(a, b, c):
    MAX=max(a,b,c)
    
    if MAX==a:
        r1, r2 = b, c
    elif MAX==b:
        r1, r2 = c, a
    else:
        r1, r2 = a, b
    
    if MAX > r1 + r2:
        return 0
    elif MAX == r1 + r2:
        return 1
    else:
        return 2

#삼각형을 만들수있어?


T=int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    DISTANCE = ((x2-x1)**2 + (y2-y1)**2)**0.5
    CHECK=triangle(DISTANCE, r1, r2)

    if CHECK==1 and DISTANCE==0:
        print(-1)
    else:
        print(CHECK)



