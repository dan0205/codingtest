L = int(input())
T = int(input())

NUM = [0] * (L+1)
RES = [0] * (T+1)

max_num, max_idx = 0, 0

for i in range(1, T+1):
    a, b = map(int, input().split())
    if b-a+1 > max_num:
        max_num, max_idx = b-a+1, i

    for j in range(a, b+1):
        if NUM[j] == 0:
            NUM[j] = i

print(max_idx)


for i in range(1, L+1):
    if NUM[i] != 0:
        RES[NUM[i]] += 1

actual_max = max(RES)
for i in range(1, T+1):
    if RES[i] == actual_max:
        print(i)
        break