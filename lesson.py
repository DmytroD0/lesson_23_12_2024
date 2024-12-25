number = int(input("Enter number: "))


a = number // 1000
b = (number % 1000) // 100
c = (number % 100) // 10
d = number % 10
print(a)
print(b)
print(c)
print(d)


code = int(input("Enter code: "))
a1 = code % 10
a2 = (code // 10) % 10
a3 = (code // 100) % 10
a4 = (code // 1000) % 10
a5 = code // 10000
a1code = a1 * 10000 + a2 * 1000 + a3 * 100 + a4 * 10 + a5
print(a1code)