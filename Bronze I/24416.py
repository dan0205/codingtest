N=int(input())

def fib(N:int) -> int:
    NUM = [1, 1]
    for i in range(2, N):
        NUM.append(NUM[i-1] + NUM[i-2])
    return NUM[N-1]

print(fib(N), N-2)

