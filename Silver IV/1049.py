N,M=map(int, input().split())
NUM=[list(map(int, input().split())) for _ in range(M)]

MIN_1 = NUM[0][1]
MIN_6 = NUM[0][0]

for i in range(1, M):
    MIN_1 = min(MIN_1, NUM[i][1])
    MIN_6 = min(MIN_6, NUM[i][0])

MIN_RES = N * MIN_1
TMP = MIN_RES

while N > 0:
    if N < 6:
        TMP -= N*MIN_1
        TMP += MIN_6
        N=0
    else:
        N -= 6
        TMP -= 6*MIN_1
        TMP += MIN_6

    if MIN_RES > TMP:
        MIN_RES = TMP

print(MIN_RES)
