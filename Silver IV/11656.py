STR=input()
LIST=[]

for i in range(len(STR)):
    LIST.append(STR[i:])

print(*sorted(LIST), sep='\n')