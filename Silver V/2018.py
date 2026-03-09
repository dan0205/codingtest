N=int(input())
RES=0
START, END, SUM = 1, 1, 1

while END <= N:
    if SUM > N:
        SUM -= START
        START += 1
    else:
        if SUM == N:
            RES += 1
        END += 1
        SUM += END

print(RES)