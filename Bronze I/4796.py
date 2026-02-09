idx=1

while True:
    L,P,V=map(int,input().split())
    if L==0:
        break

    DIV, MOD = divmod(V,P)
    res = L*DIV + min(MOD, L)
    print(f"Case {idx}: {res}")
    idx += 1



