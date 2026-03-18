import sys

N,M=map(int, input().split())
NUM=list(map(int, sys.stdin.readline().split()))


i=0
j=0
RES=0

while j<=N:
    if M == sum(NUM[i:j]):
        RES += 1
        j += 1
    elif M < sum(NUM[i:j]):
        i += 1
    else:
        j += 1
    
print(RES)









