import sympy as sp

def integral_():

    print("Power = **", end="\t\t")
    print("Multiple = *", end="\t\t")
    print("Division = /", end="\n")
    print("Logarithm = log(x)", end="\t")
    print("Ln = ln(x)", end="\t\t")
    print("e ** x = exp(x)", end="\n")
    print("\u221A = sqrt(x)")
    print("arc(tan, sin, cos, cot) = atan(x) , asin(x) , acos(x) , acot(x)")
    print("arc(tanh, sinh, cosh, coth) = atanh(x) , asinh(x) , acosh(x) , acoth(x) \n")
    print(".\n.\n.\n.\n")

    try:
        input_ = input("Enter the function: \n")
        input_variable = input("Enter the variable: ")

        exp = sp.sympify(input_)
        var = sp.Symbol(input_variable)
        integral = sp.integrate(exp, var)
        
        print("Integral:")
        c = sp.Symbol("C") 
        sp.pprint(c + integral)
        
    except (sp.SympifyError, ValueError):
        print("Enter a valid input. Pay attention to the hints\n")