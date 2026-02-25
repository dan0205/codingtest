NUM = []

idx, chk = 1, 1

while chk<=10000:

    if '666' in str(idx):
        NUM.append(idx)
        chk += 1

    idx += 1

print(NUM[int(input())-1])