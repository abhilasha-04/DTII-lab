import sympy as sp

x = sp.symbols('x') 

def calculator():
    a = input("Enter expression: ")

    if a.startswith("diff(") and a.endswith(")"):
        expr_str = a[5:-1]   
        expr = sp.sympify(expr_str)
        result = sp.diff(expr, x)
        print("Derivative:", result)

    elif a.startswith("integrate(") and a.endswith(")"):
        expr_str = a[10:-1]  
        expr = sp.sympify(expr_str)
        result = sp.integrate(expr, x)
        print("Integral:", result)

    else:
        expr = sp.sympify(a)
        result = expr.evalf()
        print("Result:", result)


calculator()