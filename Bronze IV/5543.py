li=[]
min_burger=2000
min_beverege=2000

for i in range(5):
    li.append(int(input()))

    if(i<3):
        min_burger = min(min_burger, li[i])
    else:
        min_beverege = min(min_beverege, li[i])

print(min_burger + min_beverege - 50)