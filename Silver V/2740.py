N_A,M_A = map(int, input().split())
MAT_A = [list(map(int, input().split())) for _ in range(N_A)]

N_B,M_B = map(int, input().split())
MAT_B = [list(map(int, input().split())) for _ in range(N_B)]


for i in range(0, N_A):
    for j in range(0, M_B):
        sum=0
        for k in range(0, M_A):
            sum += MAT_A[i][k]*MAT_B[k][j]
        print(sum, end=' ')
    print()
    