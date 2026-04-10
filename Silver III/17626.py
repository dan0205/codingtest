N=int(input())
DP = [0, 1, 2, 3, 1]

for i in range(5, N+1):
    MIN=10000
    for j in range(1, int(i**0.5)+1):
        if i - j*j >= 0:
            MIN = min(DP[i - j*j], MIN)
    DP.append(MIN+1)

print(DP[N])

# O(n루트(n))이라서 올바른 풀이지만, python3는 속도가 느려서 시간초과가 발생한다
# 따라서 PyPy3로 제출하자