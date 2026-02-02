import math

T=int(input())
for _ in range(T):
    A, B = map(int,input().split())
    GCD = math.gcd(A,B)
    print(A*B//GCD)
    