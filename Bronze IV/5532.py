li=[]
for i in range(5):
    n=int(input())
    li.append(n)

max_a = int(li[1]/li[3]) if li[1]%li[3]==0 else int(li[1]/li[3]+1)
max_b = int(li[2]/li[4]) if li[2]%li[4]==0 else int(li[2]/li[4]+1)
max=max(max_a, max_b)

print(li[0]-max)
