import sys

N,M=map(int, input().split())
DICT={}

for i in range(N):
    STR_A, STR_B = sys.stdin.readline().strip().split()
    DICT[STR_A] = STR_B

for i in range(M):
    STR = sys.stdin.readline().strip()
    print(DICT[STR])

