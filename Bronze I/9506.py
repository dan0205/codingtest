while True:
    N = int(input())
    if N==-1:
        break

    NUM = []
    for i in range(1, N):
        if N%i == 0:
            NUM.append(i)
    
    if sum(NUM) == N:
        NUM.sort()
        print(f"{N} = ", end='')
        print(*NUM, sep=' + ')
    else:
        print(f"{N} is NOT perfect.")