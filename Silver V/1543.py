STR = input()
ANS = input()
RES = 0
idx = STR.find(ANS)

while idx != -1:
    RES += 1
    idx = STR.find(ANS, idx+len(ANS))

print(RES)