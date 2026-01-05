max_sum=0

for i in range(2):
    a,b,c,d = map(int,input().split())
    max_sum = max(max_sum, a+b+c+d)

print(max_sum)