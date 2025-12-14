from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

t  = [0,1,2,3,4,5]
T  = [25,30,45,70,90,100]

f=interp1d(t, T, kind='quadratic')

x=np.linspace(0,5,50)
y=f(x)

plt.scatter(t, T, color='r', label='original points')
plt.plot(x, y, color='g')
plt.title('Interpolated temperature')
plt.scatter(2.7, f(2.7), color='blue', label='Estimated temperature at t=2.7')
plt.grid(True, alpha=0.7)
plt.legend()
plt.show()
