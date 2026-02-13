T=int(input())
for _ in range(T):
    N,M = map(int,input().split())
    res = 0

    for i in range(N, M+1):
        CHR = str(i)
        for C in CHR:
            if C=='0':
                res += 1
        
    print(res)

