import sympy as sp

def deriviation():
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
        input_ = input("Enter the function: \n")

        exp = sp.sympify(input_)
        var = sp.Symbol(input_variable)

        det_times = int(input("How many times do you want to detriviate the function? \n"))
        detriviation = sp.diff(exp, var,det_times)
        
        print("detriviation: ")
        sp.pprint( detriviation)
        
    except (sp.SympifyError, ValueError):
        print("Enter a valid input. Pay attention to the hints\n")
        
