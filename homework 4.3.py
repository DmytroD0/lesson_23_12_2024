import random
list1 = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print(list1)

list2 = [list1[0], list1[2], list1[-2]]
print(list2)