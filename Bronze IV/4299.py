sum,de=map(int,input().split())
#a+b=sum, a-b=de sum+de=2a, sum-de=2b 3,2 -> 5/2, 1/2

if(((sum+de)/2).is_integer() and (sum+de)/2>=0 and (sum-de)/2>=0):
    print(int((sum+de)/2), int((sum-de)/2))
else:
    print("-1")