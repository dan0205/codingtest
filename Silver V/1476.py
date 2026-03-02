

E,S,M = map(int,input().split())
NEW_E = E

while True:
    if (NEW_E - S)%28 == 0 and (NEW_E - M)%19 == 0:
        print(NEW_E)
        break
    NEW_E += 15