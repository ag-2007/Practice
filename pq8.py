import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

time=np.array([0,1,2,3,4])
glucose=np.array([95,140,170,150,120])

f=interp1d(time,glucose,kind='quadratic')

t_new=np.linspace(0,4, 10)
g_new=f(t_new)

plt.plot(time, glucose, 'o', label='data points')
plt.plot(t_new, g_new, '-', label='quadratic interpolation')
plt.xlabel('Time')
plt.ylabel('Glucose Level')
plt.legend()
plt.scatter(2.7, f(2.7), color='red')
plt.show()
