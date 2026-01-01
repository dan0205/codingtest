import sys

lines = sys.stdin.readlines()

for i in range(len(lines)):
    a, b = map(int,lines[i].split())
    print(a+b)