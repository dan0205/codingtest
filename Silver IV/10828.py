N=int(input())
COM=[input() for _ in range(N)]
RES=[]

for line in COM:
    if 'push' in line:
        command, n = line.split()
        RES.append(n)
    elif line == 'pop':
        print(-1 if len(RES)==0 else RES.pop())
    elif line == 'size':
        print(len(RES))
    elif line == 'empty':
        print(1 if len(RES)==0 else 0)
    elif line == 'top':
        print(-1 if len(RES)==0 else RES[len(RES)-1])
