L,P=map(int,input().split())
li=list(map(int,input().split()))
person_count=L*P

for i in li:
    print(i-person_count,end=' ')
