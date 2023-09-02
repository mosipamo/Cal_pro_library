import sympy as sp
import numpy as np
#∫

def definite_integral_():
    print("Power = pow", end="\t\t")
    print("Multiple = *", end="\t\t")
    print("Division = /", end="\n")
    print("Logarithm = log(x)", end="\t")
    print("Ln = ln(x)", end="\t\t")
    print("e ** x = exp(x)", end="\n")
    print("\u221A = sqrt(x)", end = "\t\t")
    print("\u221B = cbrt(x)")
    print("arc(tan, sin, cos, cot) = atan(x) , asin(x) , acos(x) , acot(x)")
    print("arc(tanh, sinh, cosh, coth) = atanh(x) , asinh(x) , acosh(x) , acoth(x) \n")
    print(".\n.\n.\n.\n")

    try:
        input_variable = input("Enter the variable: ")
        input_ = input("Enter the function: \n")
        lower_limit = input("Enter the lower limit: ")
        upper_limit = input("Enter the upper limit: ")
        
        exp = sp.sympify(input_)
        var = sp.Symbol(input_variable)
        integral = sp.integrate(exp, (var, lower_limit, upper_limit))
        
        print("Integral: ")
        sp.pprint(integral)

    except (sp.SympifyError, ValueError):
        print("Enter a valid input. Pay attention to the hints\n")