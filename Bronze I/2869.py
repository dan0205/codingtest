A,B,V = map(int,input().split())

FINAL = V-A
DAY = A-B
print((FINAL + DAY - 1) // DAY + 1)