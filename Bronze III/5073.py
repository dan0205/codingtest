while True:
    li=list(map(int,input().split()))
    sum_res = sum(li)
    set_li = set(li)
    if(set_li == {0}):
        break

    if(sum_res-max(set_li) <= max(set_li)):
        print("Invalid")
        continue

    if(len(set_li)==1):
        print("Equilateral")
    elif(len(set_li)==2):
        print("Isosceles")
    else:
        print("Scalene")