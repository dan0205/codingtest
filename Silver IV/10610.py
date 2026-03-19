N=input()

SUM=0
for i in range(len(N)):
    SUM += int(N[i])

if N.find('0') != -1 and SUM%3 == 0:
    print(*sorted(list(N), reverse=True), sep='')
else:
    print(-1)
    