def _func(NUM: list, N: int) -> int:
    res = 0
    for num in NUM:
        if N==num:
            res += 1
    
    return res

T=int(input())

for _ in range(T):
    NUM_A = list(map(int,input().split()))
    NUM_B = list(map(int,input().split()))
    flag = True

    for i in range(4, 0, -1):
        if _func(NUM_A[1:], i) == _func(NUM_B[1:], i):
            continue
        else:
            print('A' if _func(NUM_A[1:], i) > _func(NUM_B[1:], i) else 'B')
            flag = False
            break
    
    if flag:
        print('D')