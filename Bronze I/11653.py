def _find_mod(N: int) -> dict:
    for i in range(2, int(N**0.5)+1):
        if N%i == 0:
            return N//i, i
    
    return 0, N

N=int(input())

if N<=1:
    exit()

while N != 0:
    N,M = _find_mod(N)
    print(M)