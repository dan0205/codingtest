N=int(input())
NUM_A=list(map(int, input().split()))
NUM_B=list(map(int, input().split()))

NUM_A.sort(reverse=True)
NUM_B.sort()

SUM = [NUM_A[i]*NUM_B[i] for i in range(N)]
print(sum(SUM))
