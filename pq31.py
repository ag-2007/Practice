from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import math as m

def R(d):
    return -(d*(m.e)**(-0.4*d))

result=optimize.minimize_scalar(R)

x=np.linspace(0,10, 100)
y=-R(x)

plt.plot(x, y , color='b', label='Response')
plt.scatter(result.x, -R(result.x), color='red', label='Maximum Response')
plt.title("Optimal Response")
plt.xlabel('Dosage')
plt.ylabel('Response')
plt.legend()
plt.show()