N=int(input())
t_list = list(map(int,input().split()))
p_list = list(map(int,input().split()))

t_sum = 0
for t in t_list:
    a,b=divmod(t, p_list[0])
    t_sum += a if b==0 else a+1


a,b=divmod(N, p_list[1])
print(f"{t_sum}\n{a} {b}")