N=int(input())
min_time=1001

for i in range(N):
    A,B=map(int,input().split())
    if (A<=B):
        min_time = min(min_time, B)

print(min_time if min_time<=1000 else "-1")