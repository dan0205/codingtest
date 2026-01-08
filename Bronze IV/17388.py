li=list(map(int,input().split()))
if(sum(li[0:])>=100):
    print("OK")
else:
    if li.index(min(li[0:]))==0:
        print("Soongsil")
    elif li.index(min(li[0:]))==1:
        print("Korea")
    else:
        print("Hanyang")