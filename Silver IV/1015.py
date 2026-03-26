N=int(input())
NUM=list(map(int, input().split()))

RES=[]
for i, num in enumerate(NUM):
    RES.append((num, i))

SORT=sorted(RES)


P=[0]*N
for new_idx, (num, origin_idx) in enumerate(SORT):
    P[origin_idx] = new_idx

print(*P)