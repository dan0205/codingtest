x, y = map(int,input().split())

day_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
month_list = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
DAY=0

for i in range(x):
    DAY = (month_list[i] + DAY) % 7

print(day_list[(y+DAY-1)%7])