N=int(input())
length=len(str(N))
SUM=0

for i in range(1, length):
    SUM += 9 * (10**(i-1)) * i


SUM += (N - (10**(length-1)) + 1) * length

print(SUM)