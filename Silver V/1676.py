N=int(input())
RES=1
for i in range(2, N+1):
    RES *= i

res=0
for i in str(RES)[::-1]:
    if i == '0':
        res+=1
    else:
        break

print(res)