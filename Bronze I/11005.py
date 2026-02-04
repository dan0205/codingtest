BASE = [i for i in range(0, 10)]
CHAR = [chr(i) for i in range(ord('A'), ord('Z')+1)]
BASE += CHAR

N, B = map(int, input().split())
RES = []

while N>0:
    N, MOD = divmod(N,B)
    RES.append(BASE[MOD])

print(*RES[::-1], sep='')