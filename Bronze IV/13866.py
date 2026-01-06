li=list(map(int,input().split()))

li.sort(reverse=True)
print(abs(li[0]+li[3]-sum(li[1:3])))
