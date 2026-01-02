h,m,s=map(int,input().split())
time=int(input())

s+=time
if(s>=60):
    m+=int(s/60)
    s=s%60
if(m>=60):
    h+=int(m/60)
    m=m%60
while(h>=24):
    h-=24

print(f"{h} {m} {s}")