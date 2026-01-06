

A,B,C = map(int, input().split())

if(A>B):
    A,B=B,A

if(B>C):
    if(A>C):
        A,B,C=C,A,B
    else:
        B,C=C,B

print(B)

"""
1 2 3 -> 1 2 3 
1 3 2 -> 1 3 2 -> 1 2 3
2 1 3 -> 1 2 3 
2 3 1 -> 2 3 1 -> 2 1 3
3 1 2 -> 1 3 2 -> 1 2 3
3 2 1 -> 2 3 1 -> 2 1 3





"""