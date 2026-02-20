N=input()
flag = False

for i in range(1, len(N)):
    a, b = 1, 1

    for j in range(0, i):
        a *= int(N[j])
    
    for j in range(i, len(N)):
        b *= int(N[j])

    if a == b:
        flag = True
        break

print("YES" if flag else "NO")