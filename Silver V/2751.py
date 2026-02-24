import sys
input = sys.stdin.readline

N=int(input())
NUM=[int(input()) for _ in range(N)]

print(*sorted(NUM), sep='\n')