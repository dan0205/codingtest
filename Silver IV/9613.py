import math
import sys
T=int(input())

for i in range(T):
    NUM=list(map(int, sys.stdin.readline().strip().split()))
    
    GCD=0
    for i in range(1, NUM[0]):
        for j in range(i+1, NUM[0]+1):
            GCD+=math.gcd(NUM[i], NUM[j])
    
    print(GCD)