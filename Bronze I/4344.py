for i in range(int(input())):
    M, *num_list = map(int, input().split())
    MID = sum(num_list)/M
    
    cot = sum(1 for s in num_list if s > MID)

    print(f"{cot/M*100:.3f}%")