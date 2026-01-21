ascending_check_list = [1,2,3,4,5,6,7,8]
descending_check_list = sorted(ascending_check_list, reverse=True)

res_list = list(map(int,input().split()))

if res_list==ascending_check_list:
    print("ascending")
elif res_list==descending_check_list:
    print("descending")
else:
    print("mixed")