A,B,C = map(int, input().split())

if(A>B):
    A,B=B,A

if(B>C):
    if(A>C):
        A,B,C=C,A,B
    else:
        B,C=C,B

print(B)