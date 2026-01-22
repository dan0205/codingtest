T=int(input())
for i in range(T):
    a,b = map(int,input().split())
    res = pow(a,b, 10)
    print(res if res!=0 else 10)