import sympy as sp

def triple_integral_():
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
        input_variable3 = input("Enter the Third variable: ")

        input_ = input("Enter the function: \n")

        lower_limit = input(f"Enter the lower limit of {input_variable}: ")
        upper_limit = input(f"Enter the upper limit of {input_variable}: ")
        
        lower_limit2 = input(f"Enter the lower limit of {input_variable2}: ")
        upper_limit2 = input(f"Enter the upper limit of {input_variable2}: ")
        
        lower_limit3 = input(f"Enter the lower limit of {input_variable3}: ")
        upper_limit3 = input(f"Enter the upper limit of {input_variable3}: ")

        exp = sp.sympify(input_)
        var = sp.Symbol(input_variable)
        var2 = sp.Symbol(input_variable2)
        var3 = sp.Symbol(input_variable3)

        first_inner_integral = sp.integrate(exp, (var, lower_limit, upper_limit))
        second_integral = sp.integrate(first_inner_integral, (var2, lower_limit2, upper_limit2))
        third_integral = sp.integrate(second_integral, (var3, lower_limit3, upper_limit3))

        print("Integral: ")
        sp.pprint(third_integral)
        
    except (sp.SympifyError, ValueError):
        print("Enter a valid input. Pay attention to the hints\n")