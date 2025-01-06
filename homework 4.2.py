list1 = [2, 3, 4, 5, 6, 6, 7]
if len(list1) == 0:
    print(0)
else:
    operation1 = sum(list1[i] for i in range(0, len(list1), 2))
    result = operation1 * list1[-1]
    print(result)
