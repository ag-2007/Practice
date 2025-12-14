Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
Temperature = [30, 32, 31, 29, 35, 36, 33]
Humidity = [70, 65, 68, 75, 60, 55, 72]

import pandas as pd

data={'Days': Days,
      'Temperature': Temperature, 
      'Humidity': Humidity
      } 

df=pd.DataFrame(data)
print(df)

#Average temperature and humidity
avg_temprature= df['Temperature'].mean()
avg_humidity= df['Humidity'].mean()
print("Average Temperature:", avg_temprature)
print("Average Humidity:", avg_humidity)

print("\Days with temperature above average:")

for index, row in df.iterrows():
      if row['Temperature']> avg_temprature:
            print(row['Days'])

print("\nDays with Humidity below average:")
for index, row in df.iterrows():
      if row['Humidity'] < avg_humidity:
            print(row['Days'])

#Dual Line graphs
import matplotlib.pyplot as plt

fig, ax1=plt.subplots()
ax2=ax1.twinx()

ax1.plot(Days, Temperature, 'g-', label='Temperature')
ax2.plot(Days, Humidity, 'b--', label='Humidity')

ax1.set_xlabel('Days')
ax1.set_ylabel('Temperature')
ax2.set_ylabel('Humidity')

plt.title("Plot of Temperature and Humidity over the Days")
plt.show()  






