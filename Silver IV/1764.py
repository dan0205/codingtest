import sys

N,M=map(int, input().split())
SET_A=set([sys.stdin.readline().strip() for _ in range(N)])
SET_B=set([sys.stdin.readline().strip() for _ in range(M)])

print(len(SET_A & SET_B))
print(*sorted(SET_A & SET_B), sep='\n')