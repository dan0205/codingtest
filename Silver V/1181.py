T=int(input())
WORD=[input() for _ in range(T)]

print(*sorted(set(WORD), key=lambda x: (len(x), x)), sep='\n')