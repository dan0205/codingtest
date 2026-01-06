str=input()
li=['a','e','i','o','u']
result=0

for i in str:
    if(i in li):
        result+=1

print(result)