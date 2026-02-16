result = 0
expression = ""

while True:
    value = input()

    if value == "=":
        try:
            result = eval(expression)
            print("Result =", result)
        except ZeroDivisionError:
            print("Division by zero not allowed")
        except:
            print("Invalid Expression")
        break

    elif value in ["+", "-", "*", "/"]:
        expression += value

    else:
        try:
            number = int(value)
            expression += str(number)
        except:
            print("Invalid Input")