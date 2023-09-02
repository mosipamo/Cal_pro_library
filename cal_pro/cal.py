import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *

def integral_():

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
        print("Enter a valid input. \n")
        
        
def definite_integral_():
    
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
        print("Enter a valid input. \n")



def double_integral_():
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
        print("Enter a valid input. \n")
        
        



def triple_integral_():
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
        print("Enter a valid input. \n")
        
    


def deriviation():

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
        print("Enter a valid input. \n")
        
        


def simple_cal():
    
    try:
        expression = input("Enter a mathematical expression: ")

        result = eval(expression)
        print(result)
    except :
        print("Enter a valid syntax")
        



def equation():
    exp = input("Enter the equation to solve: \n")
    res = sp.solve(exp)
    print("The answer is:\n\n")

    sp.pprint(res)
    


def plot_1():
    
    try:
    
        x = sp.symbols('x')
        expr = input("Enter a function in terms of 'x': \n")
        y = sp.sympify(expr)

        # lambdify transform sympy expressions into Python functions
        # it converts the SymPy names to the names of the given numerical library, usually NumPy.
        func = sp.lambdify(x, y, "numpy")

        x_vals = np.linspace(-20, 20, 1000)
        y_vals = func(x_vals)

        plt.figure(figsize=(10, 8))
        plt.plot(x_vals, y_vals, color='red', linewidth='2')
        plt.xlabel('X_axis')
        plt.ylabel('Y_axis')
        plt.grid(True)
        plt.show()
    except (sp.SympifyError, ValueError):
        print("Enter a valid input.\n")
        
        


def plot_2():
    try:
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
        print("Enter a valid input. \n")



def plot_3():
    try:
        x = sp.symbols('x')
        expr = input("Enter the first function 'x': \n")
        expr2 = input("Enter the second function 'x': \n")
        expr3 = input("Enter the third function 'x': \n")
        y = sp.sympify(expr)
        y2 = sp.sympify(expr2)
        y3 = sp.sympify(expr3)
        # lambdify transform sympy expressions into Python functions
        # it converts the SymPy names to the names of the given numerical library, usually NumPy.
        func1 = sp.lambdify(x, y, "numpy")
        func2 = sp.lambdify(x, y2, "numpy")
        func3 = sp.lambdify(x, y3, "numpy")
        x_vals = np.linspace(-20, 20, 1000)
        y_vals = func1(x_vals)
        y_vals2 = func2(x_vals)
        y_vals3 = func3(x_vals)

        plt.figure(figsize=(10, 8))
        plt.plot(x_vals, y_vals, color='red', linewidth='2')
        plt.plot(x_vals, y_vals2, color='blue', linewidth='2')
        plt.plot(x_vals, y_vals3, color='green', linewidth='2')
        plt.xlabel('X_axis')
        plt.ylabel('Y_axis')
        plt.grid(True)
        plt.show()
    except (sp.SympifyError, ValueError):
        print("Enter a valid input. \n")
        
        
        


def plot_x_y():
    try:
   
        x,y = sp.symbols('x y')


        expr = input("Enter a function in terms of 'x,y': \n")
        fun = sp.sympify(expr)

        lambd_func = sp.lambdify((x,y), fun, 'numpy')
        x_val = np.linspace(-10, 10, 1000)
        y_val = np.linspace(-10, 10, 1000)
        X_, Y_ = np.meshgrid(x_val, y_val)  #مختصات برداری رو میاره تو ماتریس واسه کار با موقعیت ها
        Z = lambd_func(X_, Y_)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d') # projection='3d' this att is usefulto create a 3d subplot
        ax.plot_surface(X_, Y_, Z, cmap='viridis') # cmp = colormap (defines what color to use for plotting)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Double Integral Plot')
        plt.show()
    except (sp.SympifyError, ValueError):
        print("Enter a valid input. \n")




def plot_x_z():
    try:
        
        x,z = sp.symbols('x z')


        expr = input("Enter a function in terms of 'x,z': \n")
        fun = sp.sympify(expr)

        lambd_func = sp.lambdify((x,z), fun, 'numpy')
        x_val = np.linspace(-10, 10, 1000)
        z_val = np.linspace(-10, 10, 1000)
        X_, Z_ = np.meshgrid(x_val, z_val)  #مختصات برداری رو میاره تو ماتریس واسه کار با موقعیت ها
        Y = lambd_func(X_, Z_)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d') # projection='3d' this att is usefulto create a 3d subplot
        ax.plot_surface(X_,  Y, Z_, cmap='viridis') # cmp = colormap (defines what color to use for plotting)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Double Integral Plot')
        plt.show()
    except (sp.SympifyError, ValueError):
        print("Enter a valid input. \n")
        
        
        



def plot_y_z():
    try:
        y,z = sp.symbols('y z')


        expr = input("Enter a function in terms of 'y , z': \n")
        fun = sp.sympify(expr)

        lambd_func = sp.lambdify((y, z), fun, 'numpy')
        z_val = np.linspace(-10, 10, 1000)
        y_val = np.linspace(-10, 10, 1000)
        Z_, Y_ = np.meshgrid(z_val, y_val)  #مختصات برداری رو میاره تو ماتریس واسه کار با موقعیت ها
        X = lambd_func( Y_,Z_)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d') # projection='3d' this att is usefulto create a 3d subplot
        ax.plot_surface( X, Y_, Z_, cmap='viridis') # cmp = colormap (defines what color to use for plotting)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Double Integral Plot')
        plt.show()
    except (sp.SympifyError, ValueError):
        print("Enter a valid input. \n")






        
