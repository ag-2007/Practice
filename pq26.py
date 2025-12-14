from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

Time  = [0, 1, 3, 4, 6]
Speed = [0, 40, 60, 55, 70]

f=interp1d(Time, Speed, kind='cubic')

x=np.linspace(0, 6, 120)
y=f(x)

plt.scatter(Time, Speed, color='green', label='original data points')
plt.plot(x, y, color='b')
plt.scatter(2, f(2), color='red', label='Speed at t=2')
plt.scatter(5, f(5), color='yellow', label='Speed at t=5')
plt.legend()
plt.grid(True, alpha=0.7)
plt.show()

