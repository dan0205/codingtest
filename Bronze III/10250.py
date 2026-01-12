T=int(input())
for i in range(T):
    H,W,N=map(int,input().split())

    H_res = N%H if N%H!=0 else H
    W_res = N//H+1 if N%H!=0 else N//H

    print(f"{H_res}{W_res:02d}")