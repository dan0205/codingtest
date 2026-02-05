T=int(input())

for _ in range(T):
    NUM = list(map(int,input().split()))
    NUM.sort(reverse=True)
    print(NUM[2])