position = {}
for r in range(5):
    row = list(map(int, input().split()))
    for c in range(5):
        position[row[c]] = (r,c)

calls = []
for _ in range(5):
    calls.extend(list(map(int, input().split())))

row_count = [0]*5
col_count = [0]*5
diag1_count = 0
diag2_count = 0

bingo_lines = 0

for i, num in enumerate(calls):
    r, c = position[num]

    row_count[r] += 1
    col_count[c] += 1

    if row_count[r] == 5:
        bingo_lines += 1
    if col_count[c] == 5:
        bingo_lines += 1

    if r == c:
        diag1_count += 1
        if diag1_count == 5:
            bingo_lines += 1
    
    if r + c == 4:
        diag2_count += 1
        if diag2_count == 5:
            bingo_lines += 1
    
    if bingo_lines >= 3:
        print(i+1)
        break