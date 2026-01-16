score = [list(map(int,input().split())) for _ in range(5)]

idx, res = 1, sum(score[0])

for i in range(1, 5):
    if sum(score[i])>res:
        idx, res = i+1, sum(score[i])

print(idx, res)

