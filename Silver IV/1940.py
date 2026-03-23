import sys

N=int(input())
M=int(input())
NUM=list(map(int, sys.stdin.readline().strip().split()))
NUM.sort()


s_idx=0
e_idx=N-1
RES=0

while True:
    if s_idx >= e_idx:
        break

    SUM = NUM[s_idx] + NUM[e_idx]

    if SUM < M:
        s_idx += 1

    elif SUM == M:
        RES += 1
        s_idx += 1
        e_idx -= 1

    elif SUM > M:
        e_idx -= 1


print(RES)

