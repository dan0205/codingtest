import sys
input = sys.stdin.readline

num = [int(input()) for _ in range(9)]
num_sum = sum(num)

for i in range(0, 9):
    for j in range(i+1, 9):
        if num_sum-(num[i] + num[j]) == 100:
            a,b = num[i], num[j]
            num.remove(a)
            num.remove(b)
            print(*num, sep='\n')
            exit()
            
            
