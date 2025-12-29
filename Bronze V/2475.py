a = [0] * 5

a[0], a[1], a[2], a[3], a[4] = map(int, input().split())
sum=0

for i in range(5):
    sum += a[i] * a[i]
    
print(sum % 10)