A,B=map(int,input().split())
NUM = []
for i in range(1, B+1):
    [NUM.append(i) for _ in range(i)]
print(sum(NUM[A-1:B]))