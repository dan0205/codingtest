N=int(input())
DP=[[0,0],[1,0],[0,1],[1,1],[1,2],[2,3]]
#a,b -> b, a+b
for i in range(6, N+1):
    DP.append([DP[i-1][1], DP[i-1][0]+DP[i-1][1]])

print(sum(DP[N]))
