T=int(input())
li = [300, 60, 10]
res = []

for val in li:
    a,b = divmod(T, val)
    res.append(a)
    T = b

if T==0:
    print(*res)
else:
    print(-1)
