VAL = input()
NUM = [0] * 10

for n in VAL:
    NUM[int(n)] += 1

MAX=0
NUM[6] += NUM[9]

for i in range(0, 9):
    if i == 6:
        MAX = max((NUM[i]+1)//2, MAX)
    else:
        MAX = max(NUM[i], MAX)

print(MAX)

