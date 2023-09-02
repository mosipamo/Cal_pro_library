import sympy as sym 

def exp():
    exp = input("Enter the equation to solve: \n")
    res = sym.solve(exp)
    print("The answer is:\n\n")

    sym.pprint(res)
