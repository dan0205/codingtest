a,b,c=map(int,input().split())
max=max(max(a,b),c)


# 3개의 숫자 관계를 판단하기 위해선 최소 3번의 비교 과정이 필요하다
# a==b? b==c? -> 둘다 다를때 c==a?
# 하지만 파이썬 set은 중복이 불가능하기 때문에 훨씬 간단하다

numbers={a,b,c}
uniqie=len(numbers)

if uniqie==1:
    print(10000+max*1000)
elif uniqie==2:
    if(a==b):
        print(1000+a*100)
    elif(b==c):
        print(1000+b*100)
    else:
        print(1000+c*100)
else:
    print(max*100)