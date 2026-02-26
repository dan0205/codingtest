LIST = [list(input().split()) for _ in range(20)]
NUM = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

VAL1, VAL2 = 0, 0
for line in LIST:
    if line[2]!='P':
        VAL1 += float(line[1])
        VAL2 += float(line[1]) * NUM[line[2]]

print(VAL2/VAL1)