string = input()
score = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0
}
if(string=='F'):
    print("0.0")
else:
    if(string[1]=='+'):
        print(score[string[0]] + 0.3)
    elif(string[1]=='0'):
        print(score[string[0]])
    else:
        print(score[string[0]]-0.3)

