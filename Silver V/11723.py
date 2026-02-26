import sys
input = sys.stdin.readline
T=int(input())
S = set()

for i in range(T):
    line = input().split()
    INS = line[0]

    if INS == 'all':
        S = set([i for i in range(1, 21)])
        continue
    elif INS == 'empty':
        S = set()
        continue

    VAL = int(line[1])

    if INS == 'add':
        S.add(VAL)

    elif INS == 'remove':
        S.discard(VAL)

    elif INS == 'check':
        print(1 if VAL in S else 0)

    elif INS == 'toggle':
        if VAL in S:
            S.remove(VAL)
        else:
            S.add(VAL)
