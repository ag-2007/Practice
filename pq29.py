from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def C(x):
    return 0.5*(x**2)-8*x+60

result=optimize.minimize_scalar(C)

print(result)

x=np.linspace(0,20,200)
y=C(x)

plt.plot(x, y, color='g', label='Function')
plt.scatter(result.x, C(result.x), color='red', label='Optimum Point')
plt.title("Minimizing Production costs")
plt.xlabel("Units")
plt.ylabel("Cost")
plt.legend()
plt.show()