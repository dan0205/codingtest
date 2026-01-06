A,B=map(int,input().split())
C,D=map(int,input().split())

change_1 = A + D
change_2 = B + C

print(min(change_1,change_2))