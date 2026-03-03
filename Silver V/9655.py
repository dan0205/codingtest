N=int(input())
DP = [0, 'SK', 'CY', 'SK']

for i in range(4, N+1):
    if DP[i-3]=='CY' or DP[i-1]=='CY':
        DP.append('SK')
    else:
        DP.append('CY')

print(DP[N])
