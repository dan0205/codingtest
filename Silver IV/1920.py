import sys
input = sys.stdin.readline

N=int(input())
BASE=set(list(map(int, input().split())))

M=int(input())
NUM=list(map(int, input().split()))

for i in range(M):
    print(1 if NUM[i] in BASE else 0)