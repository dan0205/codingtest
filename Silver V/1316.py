def _func(STR: str) -> int:
    CHR=[0]*(ord('z')-ord('a')+1)
    
    for i in range(len(STR)):
        idx=ord(STR[i]) - ord('a')

        if CHR[idx]==0:
            CHR[idx]=1
        else:
            if idx==(ord(STR[i-1])-ord('a')):
                continue
            else:
                return 0
    
    return 1



T=int(input())
RES=0
for _ in range(T):
    RES += _func(input())

print(RES)
