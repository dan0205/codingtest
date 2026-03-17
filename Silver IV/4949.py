from collections import deque


while True:
    DEQ = deque()
    STR = input()
    if STR == '.':
        break

    flag = True
    for i in range(len(STR)):
        C = STR[i]

        if C == '(' or C == '[':
            DEQ.append(STR[i])

        elif C == ')':
            if not DEQ or DEQ.pop() != '(':
                flag = False
                break

        elif C == ']':
            if not DEQ or DEQ.pop() != '[':
                flag = False
                break

    print("yes" if flag and not DEQ else "no")
    


