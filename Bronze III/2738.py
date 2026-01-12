N,M=map(int,input().split())

li_1 = [list(map(int,input().split())) for _ in range(N)]

li_2 = [list(map(int,input().split())) for _ in range(N)]

res = [[a+b for a,b in zip(N1, N2)] for N1, N2 in zip(li_1, li_2)]

for row in res:
    print(*row)