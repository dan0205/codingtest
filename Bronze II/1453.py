N=int(input())
num_list = list(map(int,input().split()))

print(N-len(set(num_list)))