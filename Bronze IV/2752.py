#정렬 - 3개니까 내가 직접해도 되지 않을까? 최소 3번의 if가 필요하다
a,b,c=map(int,input().split())
if(a>b):
    a,b=b,a
if(b>c):
    if(a>c):
        a,b,c=c,a,b
    else:
        b,c=c,b

print(a,b,c)
