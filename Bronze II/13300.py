N,K=map(int, input().split())
std = [[0, 0] for _ in range(6)]

for i in range(N):
    a,b = map(int,input().split()) #a=0 여자 a=1 남자, b=1 1학년, b=6 6학년
    std[b-1][a] += 1

res_sum=0

for i in range(0,6):
    for j in range(0,2):
        res_sum += (std[i][j]+K-1)//K

print(res_sum)

