from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import math as m

def E(v):
    x,y=v
    return 20*x*(m.e**(-0.1*x))+200/y+0.05*x*y

result=optimize.minimize(E,x0=[0.2,2], bounds=[(0.1,50),(1,10)], method='L-BFGS-B' )
opt_x, opt_y=result.x
print("Optimal x (length):", opt_x)
print("Optimal y (thickness):", opt_y)
print("Minimum Energy Loss:", result.fun)
