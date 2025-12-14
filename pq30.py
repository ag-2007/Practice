from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def P(x):
    return -(-x**2+12*x-20)

result=optimize.minimize_scalar(P)

x=np.linspace(0,12, 120)
y=-P(x)

plt.plot(x, y , color='b', label='Profit')
plt.scatter(result.x, -P(result.x), color='red', label='Maximum Profit')
plt.title("Optimal Profit")
plt.xlabel('X')
plt.ylabel('profit')
plt.legend()
plt.show()