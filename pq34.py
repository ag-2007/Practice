from scipy.integrate import quad
import math as m
import numpy as np
import matplotlib.pyplot as plt

def T(t):
    return 100*(m.e**(-0.1*t))

result, error = quad(T, 0, 20) 

print("Total thermal energy lost =", result)
print("Error estimate=", error)

x=np.linspace(0,20,200)
y=T(x)

plt.plot(x, y, color='b', label='Total thermal energy lost over time')
plt.fill_between(x,y, alpha=0.3)
plt.axhline(30, color='gray', linestyle='--')
plt.title("Total Thermal Energy Lost")
plt.xlabel("Time")
plt.ylabel("Total Thermal Energy Lost")
plt.legend()
plt.show()