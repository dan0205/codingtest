T=int(input())

for i in range(T):
    DICT=dict()
    N=int(input())

    for j in range(N):
        a,b=input().split()
        
        if b in DICT:
            DICT[b] += 1
        else:
            DICT[b] = 1

    RES=1
    for val in DICT.values():
        RES*=(val+1)
    print(RES-1)