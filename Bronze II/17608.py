import sys
input = sys.stdin.readline

N=int(input())
num = [int(input()) for _ in range(N)]
res=0
max_height=0

for i in range(N-1, -1, -1):
    if max_height==0 or num[i] > max_height:
        max_height = num[i]
        res+=1
    
print(res)