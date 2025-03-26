value1 = int(input("enter the number : "))
value2 = int(input("enter the number : "))

operator = input("enter the operator : ")

if operator == "+":
    print(value1 + value2)
elif operator == "-":
    print(value1 - value2)
elif operator == "*":
    print(value1 * value2)
elif operator == "/":
    print(value1 / value2)
elif operator == "%":
    print(value1 % value2)
else:
    print("invalid operatorṇ")