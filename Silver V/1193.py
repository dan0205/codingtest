def _func(X: int) -> None:
    CHK=1

    for i in range(1, 1000000):
        if CHK + i < X:
            CHK += i
            continue
        else:
            for j in range(1, i+1):
                if CHK == X:
                    print(f"{j}/{i-j+1}" if i%2 == 0 else f"{i-j+1}/{j}")
                    return
                else:
                    CHK += 1
    return

_func(int(input()))