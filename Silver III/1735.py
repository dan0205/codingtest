import math
first_x, first_y = map(int, input().split())
second_x, second_y = map(int, input().split())

x = first_x*second_y + second_x*first_y
y = first_y*second_y

GCD = math.gcd(x, y)

print(x//GCD, y//GCD)
