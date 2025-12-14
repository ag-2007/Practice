from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

Seconds = np.array([0, 10, 25, 40, 55])
HR      = np.array([72, 78, 90, 85, 80])

f=interp1d(Seconds, HR, kind='linear')

x=np.linspace(0,55, 55)
y=f(x)

count=0

for i in range(56):
    if f(i)>=85:
        count+=1

print(f"The no. of times where 85 bpm was exceeded was {count} ")

plt.plot(x, y, color='r', label='heart rate')
plt.title('Heart Rate Monitoring')
plt.grid(True, alpha=0.7)
plt.legend()
plt.xlabel('Seconds')
plt.ylabel('Heart Rate/bpm')
plt.show()