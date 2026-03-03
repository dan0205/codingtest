STR=input()
LIST=[STR[0]]

for i in range(1, len(STR)):
    if STR[i-1] == STR[i]:
        continue
    else:
        LIST.append(STR[i])


NUM = [0, 0]
for n in LIST:
    if n == '0':
        NUM[0] += 1
    else:
        NUM[1] += 1

print(min(NUM))