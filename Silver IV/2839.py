N=int(input())

DP=[[-1,-1], [-1,-1], [-1,-1], [1,0], [-1,-1], [0,1], [2,0]] # 0부터 시작

for i in range(7, N+1):
    if DP[i-3][0] == -1 and DP[i-5][0] == -1:
        DP.append([-1,-1])
    elif DP[i-3][0] == -1 and DP[i-5][0] != -1:
        DP.append([DP[i-5][0], DP[i-5][1]+1])
    elif DP[i-3][0] != -1 and DP[i-5][0] == -1:
        DP.append([DP[i-3][0]+1, DP[i-3][1]])
    else:
        SUM_3 = sum(DP[i-3])
        SUM_5 = sum(DP[i-5])
        if SUM_3 < SUM_5:
            DP.append([DP[i-3][0]+1, DP[i-3][1]])
        else:
            DP.append([DP[i-5][0], DP[i-5][1]+1])



if DP[N][0] == -1:
    print(-1)
else:
    print(sum(DP[N]))




