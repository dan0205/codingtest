STR=input()
RES = STR.replace('XXXX','AAAA').replace('XX', 'BB')

print('-1' if 'X' in RES else RES)