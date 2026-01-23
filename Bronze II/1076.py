color_dict = {
    "black": {"val1": 0, "val2": 1},
    "brown": {"val1": 1, "val2": 10},
    "red": {"val1": 2, "val2": 100},
    "orange": {"val1": 3, "val2": 1000},
    "yellow": {"val1": 4, "val2": 10000},
    "green": {"val1": 5, "val2": 100000},
    "blue": {"val1": 6, "val2": 1000000},
    "violet": {"val1": 7, "val2": 10000000},
    "grey": {"val1": 8, "val2": 100000000},
    "white": {"val1": 9, "val2": 1000000000}
}

input_list = [input() for _ in range(3)]
print((color_dict[input_list[0]]['val1'] * 10 + color_dict[input_list[1]]['val1']) * color_dict[input_list[2]]['val2'])