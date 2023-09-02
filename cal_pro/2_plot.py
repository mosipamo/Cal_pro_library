import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def plot_2():
    try:
        print ("Power = **", end="\t\t")
        print ("Multiple = *", end="\t\t")
        print ("Division = /", end="\n")
        print ("Logarithm = log(x)", end="\t")
        print ("Ln = ln(x)", end="\t\t")
        print ("e ** x = exp(x)", end="\n")
        print("\u221A = sqrt(x)")
        print ("arc(tan, sin, cos, cot) = atan(x) , asin(x) , acos(x) , acot(x)")
        print ("arc(tanh, sinh, cosh, coth) = atanh(x) , asinh(x) , acosh(x) , acoth(x) \n")
        print(".\n.\n.\n.\n")


        x = sp.symbols('x')
        expr = input("Enter the first function 'x': \n")
        expr2 = input("Enter the second function 'x': \n")
        y = sp.sympify(expr)
        y2 = sp.sympify(expr2)

        # lambdify transform sympy expressions into Python functions
        # it converts the SymPy names to the names of the given numerical library, usually NumPy.
        func1 = sp.lambdify(x, y, "numpy")
        func2 = sp.lambdify(x, y2, "numpy")

        x_vals = np.linspace(-20, 20, 1000)
        y_vals = func1(x_vals)
        y_vals2 = func2(x_vals)

        plt.figure(figsize=(10, 8))
        plt.plot(x_vals, y_vals, color='red', linewidth='2')
        plt.plot(x_vals, y_vals2, color='blue', linewidth='2')
        plt.xlabel('X_axis')
        plt.ylabel('Y_axis')
        plt.grid(True)
        plt.show()
    except (sp.SympifyError, ValueError):
        print("Enter a valid input. Pay attention to the hints\n")


