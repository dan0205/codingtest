def rev(x_str: str) -> str:
    return x_str[::-1]

x_str, y_str = input().split()
x_str, y_str = rev(x_str), rev(y_str)
print(int(rev(str(int(x_str) + int(y_str)))))


