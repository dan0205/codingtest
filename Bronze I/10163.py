T = int(input())
NUM = [[0 for i in range(1001)] for j in range(1001)]


for n in range(T):
    a,b,c,d = map(int,input().split())

    for i in range(a, a+c):
        NUM[i][b:b+d] = [n+1] * d
            
RES = [0] * (T+1)
for row in NUM:
    for cell in row:
        RES[cell] += 1


for i in range(T):
    print(RES[i+1])
