MO = ['a','e','i','o','u']
while True:
    STR = input()
    if STR == 'end':
        break

    bool = True
    if not any(char in STR for char in MO):
        bool = False

    TMP = ''
    for C in STR:
        if C in MO:
            TMP += '0'
        else:
            TMP += '1'
    
    if '000' in TMP or '111' in TMP:
        bool = False
    
    for i in range(1, len(STR)):
        if STR[i-1]==STR[i] and STR[i]!='e' and STR[i]!='o':
            bool = False
            break
    
    print(f"<{STR}> is acceptable." if bool else f"<{STR}> is not acceptable.")