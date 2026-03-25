import sys

DICT={}

N=int(sys.stdin.readline())
for i in range(N):
    n=int(sys.stdin.readline())
    if n not in DICT:
        DICT[n] = 1
    else:
        DICT[n] += 1

print(max(sorted(DICT), key=DICT.get))