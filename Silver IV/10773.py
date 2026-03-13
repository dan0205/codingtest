N=int(input())
NUM=[]
for i in range(N):
    n = int(input())
    if n == 0:
        NUM.pop()
    else:
        NUM.append(n)

print(sum(NUM))