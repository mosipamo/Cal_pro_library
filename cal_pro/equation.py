from math import *

def simple_cal():
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
        expression = input("Enter a mathematical expression: ")

        result = eval(expression)
        print(result)
    except :
        print("Enter a valid syntax")

