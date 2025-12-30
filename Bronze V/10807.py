n=int(input())
li=list(map(int, input().split()))
v=int(input())
sum=0
for i in range(n):
    if(li[i]==v):
        sum+=1


print(sum)