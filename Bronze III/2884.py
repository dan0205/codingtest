H,M=map(int,input().split())

M-=45
# m>=45 -> ok
# 45>m -> (-?) -> + 60M, - 1H -> H>0 -> ok, H==0 -> 23

if(M>=0):
    print(H, M)
else:
    M+=60
    H-=1
    if(H==-1):
        H=23
    print(H, M)
