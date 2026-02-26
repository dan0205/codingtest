N=int(input())
NUM1 = set(list(map(int, input().split())))
M=int(input())
NUM2 = list(map(int,input().split()))

for n in NUM2:
    print(1 if n in NUM1 else 0, end=' ')