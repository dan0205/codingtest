T=int(input())
DANCE=['ChongChong']

COUNT=0
for i in range(T):
    A,B=input().split()

    if A in DANCE and B not in DANCE:
        COUNT += 1
        DANCE.append(B)
    elif B in DANCE and A not in DANCE:
        COUNT += 1
        DANCE.append(A)

print(len(DANCE))
    
