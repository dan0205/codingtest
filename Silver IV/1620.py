import sys


N,M=map(int,input().split())

NAME_NUM={}
NUM_NAME=[]

for i in range(N):
    STR=sys.stdin.readline().strip()
    NUM_NAME.append(STR)
    NAME_NUM[STR] = i

for i in range(M):
    query=sys.stdin.readline().strip()
    if query.isdigit():
        print(NUM_NAME[int(query)-1])
    else:
        print(NAME_NUM[query]+1)