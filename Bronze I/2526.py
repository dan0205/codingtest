N,P = map(int,input().split())

history = [N]
i = 0

while True:
    NUM = history[i] * N % P
    if NUM in history:
        print(i - history.index(NUM) + 1)
        break

    history.append(NUM)
    i += 1

