NUM=[int(input()) for _ in range(8)]
ANS=sorted(NUM, reverse=True)[:5]
print(sum(ANS))
for i in range(len(NUM)):
    if NUM[i] in ANS:
        print(i+1, end=' ')