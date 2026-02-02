""" 
2층 1명 4명 10명 20명 
1층 1명 3명 6명 10명 15명 21명
0층 1명 2명 3명 4명 5명 6명 ...

 """

T=int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    num_list = [[i for i in range(0, n+1)] for _ in range(0, k+1)]

    for i in range(1, k+1):
        for j in range(1, n+1):
            num_list[i][j] = num_list[i-1][j] + num_list[i][j-1]
          
    print(num_list[k][n])




