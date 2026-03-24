import math
import sys
N=int(input())
NUM=[]

FIRST=int(sys.stdin.readline())
for i in range(1, N):
    SECOND=int(sys.stdin.readline())
    NUM.append(SECOND-FIRST)
    FIRST=SECOND

GCD=math.gcd(*NUM)
RES=0

for n in NUM:
    RES += n//GCD - 1


print(RES)

