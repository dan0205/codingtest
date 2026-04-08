import sys
N=int(sys.stdin.readline())

# 1, 11 00,  111 100 001,   1111 1100 0011 1001 0000
# 1   2       3              5

# 11100 10000 00100
# 11111 11001 00111 10011 00001
# i-2에서 00 추가, i-1에서 1 추가 -> i-2 + i-1

DP=[0,1,2,3,5]
for i in range(5,N+1):
    DP.append((DP[i-2]+DP[i-1])%15746)

print(DP[N])