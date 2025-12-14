import matplotlib.pyplot as plt
import pandas as pd

Days    = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
Visitors= [1500, 1600, 1700, 1800, 2500, 3200, 2900]

data={'Days':Days, 
      'Visitors': Visitors}

df=pd.DataFrame(data)

df.plot(x='Days', y='Visitors', kind='line', title='Traffic Vis')
df.plot(x='Days', y='Visitors', kind='bar', title='Traffic Vis')
plt.xlabel('Days')
plt.ylabel('Visitors')
plt.show()
