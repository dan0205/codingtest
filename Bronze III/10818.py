N=int(input())
num_min = 1000000
num_max = -1000000

li=list(map(int, input().split()))

for i in li:
    num_min = min(num_min, i)
    num_max = max(num_max, i)

print(num_min, num_max)