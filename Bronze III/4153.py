while True:
    li=list(map(int,input().split()))

    if (li[0]==0 and li[1]==0 and li[2]==0):
        break;

    if(pow(li[0],2) + pow(li[1],2) + pow(li[2],2) == 2 * pow(max(li), 2)):
        print("right")
    else:
        print("wrong")
    