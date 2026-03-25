import sys

N=int(sys.stdin.readline())
SET=set()
RES=0
for i in range(N):
    STR=sys.stdin.readline().strip()

    if STR=='ENTER':
        RES += len(SET)
        SET = set()
    else:
        SET.add(STR)
    
print(RES if not SET else RES+len(SET))