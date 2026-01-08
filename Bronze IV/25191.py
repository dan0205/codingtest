N=int(input())
A,B=map(int,input().split())
min_chicken=min(N, A//2 + B)
print(min_chicken)