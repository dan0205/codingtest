N,M=map(int,input().split())
NUM_A = list(map(int,input().split()))
NUM_B = list(map(int,input().split()))

print(*sorted(NUM_A + NUM_B))