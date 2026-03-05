N=int(input())
MIN=100000

for i in range(0, N+1, 5):
    if (N-i)%2 == 0:
        MIN = min(MIN, (i//5 + (N-i)//2))


print(MIN if MIN!=100000 else -1)