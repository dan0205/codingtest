N=int(input())
res=0

for i in range(1, N+1):
    if i + sum(map(int, str(i))) == N:
        res = i
        break

print(res)