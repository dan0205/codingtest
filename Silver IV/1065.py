N=int(input())

def CHECK(STR: str) -> int:
    for i in range(1, len(STR)):
        if int(STR[1]) - int(STR[0]) != int(STR[i]) - int(STR[i-1]):
            return 0
    return 1

COUNT = N
if N > 99:
    COUNT = 99
    for i in range(100, N+1):
        COUNT += CHECK(str(i))
    
print(COUNT)