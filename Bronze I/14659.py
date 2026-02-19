import sys
input = sys.stdin.readline

N=int(input())
NUM = list(map(int,input().split()))
RES_C, RES_M = 0, 0
height = 0

for i in range(N):
    if NUM[i] > height:
        RES_M = max(RES_C, RES_M)
        height = NUM[i]
        RES_C = 0

    else:
        RES_C += 1


print(max(RES_C, RES_M))