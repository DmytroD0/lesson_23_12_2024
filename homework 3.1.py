number1 = int(input("Enter number1 "))
diya = input("Enter diya ")
number2 = int(input("Enter number2 "))
if diya == "+":
     print (number1 + number2)
elif diya == "*":
     print (number1 * number2)
elif diya == "-":
     print (number1 - number2)
elif diya == "/":
     if number2 != 0:
        print (number1 / number2)
     else:
         print("Помилка")