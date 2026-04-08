S=input()



# ababc 01234
# 0 1 2 3 4 -> (0,1) (1,2) (2,3) ... (4,5)
# 01 12 23 34 -> (0,2) (1,3) (2,4) (3,5)

SET=set()
for i in range(1, len(S)+1):
    for j in range(0, len(S)-i+1):
        SET.add(S[j:j+i])

print(len(SET))