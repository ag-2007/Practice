from scipy import optimize
import matplotlib.pyplot as plt
import math as m
import numpy as np

def E(d): 
    return -1*d*(m.e)**(-0.1*d) 

result=optimize.minimize_scalar(E) 
d_values=np.arange(0,51)
E_values=[-1*E(d) for d in d_values] 
plt.plot(d_values, E_values) 
plt.scatter(result.x, -1*E(result.x), color='red') 
plt.show()