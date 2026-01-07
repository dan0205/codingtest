# O O O X - O O -> O O X X
# X X X X ... - O O O O ... -> 
"""

3개와 2개 중 최소값
1개와 2개 중 최소값


0개와 10개 중 최소
10개와 0개 중 최소


"""

a,b,c=map(int,input().split())

print(min(b, c)+min(a-b,a-c))