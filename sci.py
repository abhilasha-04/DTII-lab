import math

def scientific_calculator():
    print("Scientific Calculator")
    print("Available operations:")
    print(" add, subtract, multiply, divide, power")
    print(" sin, cos, tan, asin, acos, atan")
    print(" log, log10, sqrt, exp")
    print(" factorial, perm, comb")
    print(" radians, degrees")
    print(" Constants: pi, e")
    print("Type 'exit' to quit")

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

            elif operation in ["sin", "cos", "tan", "asin", "acos", "atan",
                               "log", "log10", "sqrt", "exp",
                               "factorial", "radians", "degrees"]:
                x = float(input("Enter number: "))
                if operation == "sin":
                    print("Result:", math.sin(math.radians(x)))
                elif operation == "cos":
                    print("Result:", math.cos(math.radians(x)))
                elif operation == "tan":
                    print("Result:", math.tan(math.radians(x)))
                elif operation == "asin":
                    print("Result:", math.degrees(math.asin(x)))
                elif operation == "acos":
                    print("Result:", math.degrees(math.acos(x)))
                elif operation == "atan":
                    print("Result:", math.degrees(math.atan(x)))
                elif operation == "log":
                    print("Result:", math.log(x))
                elif operation == "log10":
                    print("Result:", math.log10(x))
                elif operation == "sqrt":
                    print("Result:", math.sqrt(x))
                elif operation == "exp":
                    print("Result:", math.exp(x))
                elif operation == "factorial":
                    print("Result:", math.factorial(int(x)))
                elif operation == "radians":
                    print("Result:", math.radians(x))
                elif operation == "degrees":
                    print("Result:", math.degrees(x))

            elif operation in ["perm", "comb"]:
                n = int(input("Enter n: "))
                r = int(input("Enter r: "))
                if operation == "perm":
                    print("Result:", math.perm(n, r))
                elif operation == "comb":
                    print("Result:", math.comb(n, r))

            elif operation == "pi":
                print("Result:", math.pi)
            elif operation == "e":
                print("Result:", math.e)
            else:
                print("Invalid operation. Try again.")

        except Exception as e:
            print("Error:", e)

scientific_calculator()