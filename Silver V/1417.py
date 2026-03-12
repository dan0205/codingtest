N=int(input())
PER=[int(input()) for _ in range(N)]
RES=0


if N > 1:
    ME, OTHER = PER[0], PER[1:]

    while ME <= max(OTHER):
        OTHER[OTHER.index(max(OTHER))] -= 1
        ME += 1
        RES += 1
    print(RES)

else:
    print(RES)

