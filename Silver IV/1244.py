N=int(input())
SWITCH=[0]
SWITCH.extend((map(int, input().split())))
M=int(input())
STUDENT=[list(map(int,input().split())) for _ in range(M)]

def man(idx: int):
    for i in range(idx, N+1, idx):
        SWITCH[i] = 1 - SWITCH[i]

def woman(idx: int):
    SWITCH[idx] = 1 - SWITCH[idx]

    for i in range(idx+1, N+1):
        if idx*2-i < 1:
            break

        if SWITCH[(idx*2)-i] == SWITCH[i]:
            if SWITCH[i] == 0:
                SWITCH[((idx*2)-i)], SWITCH[i] = 1, 1
            else:
                SWITCH[((idx*2)-i)], SWITCH[i] = 0, 0
        else:
            break

for i in range(M):
    if STUDENT[i][0]==1:
        man(STUDENT[i][1])
    else:
        woman(STUDENT[i][1])


for i in range(1, N+1, 20):
    print(*SWITCH[i: i+20])







