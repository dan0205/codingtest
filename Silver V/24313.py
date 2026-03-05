A,B = map(int,input().split())
C = int(input())
N = int(input())

RES = A*N + B
RES_2 = C*N

print(1 if RES<=RES_2 and A<=C else 0)