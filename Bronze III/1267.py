N=int(input())
times = list(map(int,input().split()))

min_Y, min_M = 0, 0

for time in times:
    a,b = divmod(time, 30)
    min_Y += (a+1)*10
    c,d = divmod(time, 60)
    min_M += (c+1)*15

if min_Y>min_M:
    print("M", min_M)
elif min_M>min_Y:
    print("Y", min_Y)
else:
    print("Y M", min_Y)
