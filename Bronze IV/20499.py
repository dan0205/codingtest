val=list(map(int, input().split('/')))
print("hasu" if (val[0]+val[2]<val[1] or val[1]==0) else "gosu")