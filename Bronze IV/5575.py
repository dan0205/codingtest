for i in range(3):
    start_h, start_m, start_s, finish_h, finish_m, finish_s = map(int,input().split())

    result_h = finish_h - start_h
    result_m = finish_m - start_m
    result_s = finish_s - start_s

    while (result_s>=60):
        result_s -= 60
        result_m += 1
    
    while (result_s<0):
        result_s += 60
        result_m -= 1
    
    while (result_m>=60):
        result_m -= 60
        result_h += 1

    while (result_m<0):
        result_m += 60
        result_h -= 1

    print(f"{result_h} {result_m} {result_s}")
