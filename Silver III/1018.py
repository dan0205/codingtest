ROW,COL=map(int, input().split())
NUM=[input() for _ in range(ROW)]

BASE_1,BASE_2 = [], []
for i in range(4):
    BASE_1.append('BWBWBWBW')
    BASE_1.append('WBWBWBWB')    
    BASE_2.append('WBWBWBWB')
    BASE_2.append('BWBWBWBW')

def _func(BASE):
    COUNT_1, COUNT_2 = 0, 0
    for i in range(8):
        for j in range(8):
            if BASE[i][j] != BASE_1[i][j]:
                COUNT_1 += 1
            if BASE[i][j] != BASE_2[i][j]:
                COUNT_2 += 1
    return min(COUNT_1, COUNT_2)

RES=64
for row in range(0, ROW-7):
    for col in range(0, COL-7):
        BASE=[]
        for i in range(row, row+8):
            BASE.append(NUM[i][col:col+8])
        RES=min(RES, _func(BASE))

print(RES)




