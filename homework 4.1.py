list1 =[0, 1, 0, 0, 12, 3, 6]

result = [num for num in list1 if num != 0] + [0] * list1.count(0)

print(result) 