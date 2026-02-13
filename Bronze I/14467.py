T=int(input())
COW = [-1]*11
res = 0

for _ in range(T):
    N, M = map(int,input().split())
    
    if COW[N]!=M and COW[N]!=-1:
        res += 1
    
    COW[N]=M

print(res)