T=int(input())
for i in range(T):
    a, b = input().split()
    a = int(a)
    print(''.join(a*b for b in b))