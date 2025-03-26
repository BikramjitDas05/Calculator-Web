def calculator():
    while True:
        expression = input("enter expression : ")
        if expression.lower() == exit:
            print("calculating the expression")
            break

        result = eval(expression)
        print("Result : ", result)

calculator()
