from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

Time    = np.array([0, 2, 4, 6, 8])
Glucose = np.array([85, 120, 150, 130, 110])

f=interp1d(Time, Glucose, kind='cubic')

x_new=np.linspace(0,8, 50)
y=f(x_new)
plt.scatter(Time, Glucose, color='red', marker='o', label='original data points')
plt.plot(x_new, y, color='g')
plt.title('Interpolated Glucose')
plt.scatter(3.5, f(3.5), color='blue', label='estimated glucose at 3.5 hours')
plt.xlabel('Time')
plt.ylabel('Glucose')
plt.legend()
plt.show()
