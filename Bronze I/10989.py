import sys
input = sys.stdin.readline

N=int(input())
num_list = [0] * 10001
for i in range(N):
    num = int(input())
    num_list[num] += 1

for i in range(len(num_list)):
    for _ in range(0, num_list[i]):
        print(i)