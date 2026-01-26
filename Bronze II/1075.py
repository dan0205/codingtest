N,F = [input() for _ in range(2)]

N = N[:len(N)-2] + "00"

for i in range(0, 100):
    if((int(N) + i) % int(F) == 0):
        N = str(int(N) + i)
        print(N[len(N)-2:])
        break


