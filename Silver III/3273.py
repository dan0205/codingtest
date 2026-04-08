import sys
N=int(input())
NUM=list(map(int, sys.stdin.readline().strip().split()))
NUM.sort()
X=int(input())

left, right, RES = 0, N-1, 0

while left<right:
    if NUM[left] + NUM[right] < X:
        left += 1
    elif NUM[left] + NUM[right] > X:
        right -= 1
    else:
        left += 1
        right -= 1
        RES += 1
    
print(RES)