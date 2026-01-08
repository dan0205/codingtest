string=input()
target="MOBIS"
flag=True

for i in target:
    if i not in string:
        flag=False
        break

print("YES" if flag==True else "NO")