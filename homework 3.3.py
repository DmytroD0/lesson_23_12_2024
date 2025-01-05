any_list = [1, 2, 3, 4, 5]

mid_index = (len(any_list) + 1) // 2
result = [any_list[:mid_index], any_list[mid_index:]]

print(result)