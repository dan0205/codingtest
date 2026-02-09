def _func(a:int, b:int, c:int) -> int:
    MAX = max(a,b,c)
    while True:
        if MAX%a==0 and MAX%b==0 and MAX%c==0:
            return MAX
        
        MAX += 1


NUM = list(map(int,input().split()))
MIN = _func(*NUM[0:3])

for i in range(0, 3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            MIN = min(MIN, _func(NUM[i],NUM[j],NUM[k]))

print(MIN)