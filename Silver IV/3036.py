import math
N=int(input())
NUM=list(map(int, input().split()))

first=NUM[0]

for i in range(1, N):
    current=NUM[i]
    GCD=math.gcd(first, current)
    print(f"{int(first/GCD)}/{int(current/GCD)}")
