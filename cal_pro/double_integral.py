import sympy as sp

def double_integral_():
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
        input_variable = input("Enter the First variable: ")
        input_variable2 = input("Enter the Second variable: ")
        input_ = input("Enter the function: \n")
        lower_limit = input(f"Enter the lower limit of {input_variable}: ")
        upper_limit = input(f"Enter the upper limit of {input_variable}: ")
        lower_limit2 = input(f"Enter the lower limit of {input_variable2}: ")
        upper_limit2 = input(f"Enter the upper limit of {input_variable2}: ")
        
        exp = sp.sympify(input_)
        var = sp.Symbol(input_variable)
        var2 = sp.Symbol(input_variable2)
        integ = sp.integrate(exp, (var, lower_limit, upper_limit))
        integral = sp.integrate(integ, (var2, lower_limit2, upper_limit2))
        
        print("Integral: ")
        sp.pprint (eval(integral))
        
    except (sp.SympifyError, ValueError):
        print("Enter a valid input. Pay attention to the hints\n")