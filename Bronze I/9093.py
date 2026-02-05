T=int(input())

for i in range(T):
    STR = list(input().split())
    for j in range(len(STR)):
        print(STR[j][::-1], end=' ')

