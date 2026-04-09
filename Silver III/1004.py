T=int(input())

def func(x, y, Rx, Ry, R):
    # 점과 점 사이의 거리보다 반지름이 크면 -> 안에 들어가있음
    DIS = (Rx-x)**2 + (Ry-y)**2
    if DIS <= R**2:
        return 1
    else:
        return 0




for i in range(T):
    x1,y1,x2,y2 = map(int, input().split())
    N=int(input())

    # 출발점과 도착점을 원이 둘러쌓고 있는지를 체크하자
    # 둘 다 동시에 둘러쌓고 있으면 아니고
    # 하나만 둘러쌓으면 포함이다

    RES=0
    for i in range(N):
        Rx, Ry, R = map(int, input().split())
        a = func(x1,y1,Rx,Ry,R)
        b = func(x2,y2,Rx,Ry,R)

        if (a and not b) or (not a and b):
            RES+=1
    print(RES)
