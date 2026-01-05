N=int(input())

li = list(map(int, input().split()))
sum=0

for i in range(5):
    if(li[i] == N%10):
        sum += 1

print(sum)