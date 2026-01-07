li = [list(map(int,input().split())) for i in range(2)]

if (li[1][0]>li[0][0]):
    print(li[1][0]-li[0][0] if ((li[1][1]*100+li[1][2]) - (li[0][1]*100+li[0][2]) >= 0) else li[1][0]-li[0][0] - 1)
else:
    print("0")

print(li[1][0]-li[0][0]+1)

print(li[1][0]-li[0][0])