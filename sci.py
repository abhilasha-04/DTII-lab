import math

def scientific_calculator():
    print("Scientific Calculator")
    print("Available operations: add, subtract, multiply, divide, sin, cos, tan, log, sqrt, power")

    while True:
        operation = input("\nEnter operation (or 'exit' to quit): ").lower()
        if operation == "exit":
            print("Goodbye!")
            break

        try:
            if operation in ["add", "subtract", "multiply", "divide", "power"]:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                if operation == "add":
                    print("Result:", x + y)
                elif operation == "subtract":
                    print("Result:", x - y)
                elif operation == "multiply":
                    print("Result:", x * y)
                elif operation == "divide":
                    print("Result:", x / y)
                elif operation == "power":
                    print("Result:", math.pow(x, y))

            elif operation in ["sin", "cos", "tan", "log", "sqrt"]:
                x = float(input("Enter number: "))
                if operation == "sin":
                    print("Result:", math.sin(math.radians(x)))
                elif operation == "cos":
                    print("Result:", math.cos(math.radians(x)))
                elif operation == "tan":
                    print("Result:", math.tan(math.radians(x)))
                elif operation == "log":
                    print("Result:", math.log(x))
                elif operation == "sqrt":
                    print("Result:", math.sqrt(x))
            else:
                print("Invalid operation. Try again.")
        except Exception as e:
            print("Error:", e)

scientific_calculator()