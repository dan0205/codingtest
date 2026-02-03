def _fun(string:str) -> str:
    L = len(string)
    flag = "yes"
    for i in range(0, int(L/2)+1):
        if string[i] != string[L-1-i]:
            flag = "no"
            break
    
    return flag


while True:
    string = input()
    if string == '0':
        break

    print(_fun(string))