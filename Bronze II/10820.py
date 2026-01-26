import sys


for line in sys.stdin:
    num_list = [0] * 4
    for idx in range(len(line)):
        if ord(line[idx]) >= ord('a') and ord('z') >= ord(line[idx]):
            num_list[0] += 1
        elif ord(line[idx]) >= ord('A') and ord('Z') >= ord(line[idx]):
            num_list[1] += 1
        elif ord(line[idx]) >= ord('0') and ord('9') >= ord(line[idx]):
            num_list[2] += 1
        elif line[idx] == ' ':
            num_list[3] += 1
    
    print(*num_list)