A,B=map(int,input().split())
MUL = A * B

while A%B != 0:
    A,B = B, A%B

GCD = B
LCM = MUL // GCD

print(GCD, LCM, sep='\n')
