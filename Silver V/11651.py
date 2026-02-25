T=int(input())
NUM = [list(map(int, input().split())) for _ in range(T)]

for line in sorted(NUM, key= lambda x: (x[1], x[0])):
    print(*line)