number = int(input("Enter number: "))


a = number // 1000
b = (number % 1000) // 100
c = (number % 100) // 10
e = number % 10
print(a)
print(b)
print(c)
print(e)