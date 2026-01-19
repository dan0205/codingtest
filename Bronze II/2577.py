li = [int(input()) for _ in range(3)]
res = li[0] * li[1] * li[2]
res = str(res)

for i in range(10):
    print(res.count(str(i)))