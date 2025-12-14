import pandas as pd
import matplotlib.pyplot as plt

Days      = [1,2,3,4,5,6,7]
Temp      = [28, 30, 31, 33, 32, 29, 27]
Humidity  = [70, 68, 60, 55, 58, 65, 72]

fig, ax1=plt.subplots()

ax2=ax1.twinx()

ax1.plot(Days, Temp, 'g-', label='Temperature')
ax2.plot(Days, Humidity, 'b--', label='Humidity')

plt.title("Temperature and Humidity plot")
ax1.set_xlabel("Days")
ax1.set_ylabel("Temperature")
ax2.set_ylabel("Humidity")
plt.show()


