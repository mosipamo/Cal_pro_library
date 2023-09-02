import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp 

def plot_x_z():
    try:
        print ("Power = pow", end="\t\t")
        print ("Multiple = *", end="\t\t")
        print ("Division = /", end="\n")
        print ("Logarithm = log(x)", end="\t")
        print ("Ln = ln(x)", end="\t\t")
        print ("e ** x = exp(x)", end="\n")
        print("\u221A = sqrt(x)", end = "\t\t")
        print("\u221B = cbrt(x)")
        print ("arc(tan, sin, cos, cot) = atan(x) , asin(x) , acos(x) , acot(x)")
        print ("arc(tanh, sinh, cosh, coth) = atanh(x) , asinh(x) , acosh(x) , acoth(x) \n")
        print(".\n.\n.\n.\n")
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
        print("Enter a valid input. Pay attention to the hints\n")
