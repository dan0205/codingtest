T=int(input())
NUM = [list(map(int, input().split())) for _ in range(T)]

for line in sorted(NUM):
    print(*line)