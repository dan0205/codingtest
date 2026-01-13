li_x = []
li_y = []

for i in range(3):
    a,b=map(int,input().split())
    li_x.append(a)
    li_y.append(b)

print(*(x for x in li_x if li_x.count(x)==1), end=' ')
print(*(y for y in li_y if li_y.count(y)==1))