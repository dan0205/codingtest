N=int(input())
str=input()
sum=0


for i in range(N):
    sum += ord(str[i])-48

print(sum)
    