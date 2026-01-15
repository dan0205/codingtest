res_dict = {
    "0": "E",
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D"
}

for i in range(3):
    li = list(map(int,input().split()))
    print(res_dict[str(li.count(0))])
    