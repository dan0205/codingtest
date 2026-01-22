N,K=map(int,input().split())
x_list = list(map(int,input().split()))
x_list.sort(reverse=True)

print(x_list[K-1])