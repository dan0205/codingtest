N=int(input())

for i in range(N):
    print('*' * (i+1),end='')
    print(' ' * (N-1-i),end='')
    print(' ' * (N-1-i),end='')
    print('*' * (i+1))

for i in range(1, N):
    print('*' * (N-i),end='')
    print(' ' * i, end='')
    print(' ' * i, end='')
    print('*' * (N-i))