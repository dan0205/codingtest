def _bubble(NUM: list) -> list:
    for i in range(1, len(NUM)):
        if NUM[i-1] > NUM[i]:
            NUM[i-1], NUM[i] = NUM[i], NUM[i-1]
            print(*NUM)
    
    return NUM


NUM = list(map(int,input().split()))


while NUM!=sorted(NUM):
    NUM = _bubble(NUM)



