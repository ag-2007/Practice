import matplotlib.pyplot as plt
import pandas as pd

Quarters = ["Q1","Q2","Q3","Q4"]
North    = [15,18,21,20]
South    = [10,12,14,16]
West     = [8,11,13,15]

data={'Quarters':Quarters, 
      'North': North, 
      'South':South, 
      'West':West}

df=pd.DataFrame(data)

df.plot(x='Quarters', y=['North', 'South', 'West'], kind='bar', title='Quarterly Revenue Comparison')
plt.xlabel('Quarter')
plt.ylabel('Regions')
plt.legend(['North', 'South', 'West'])
plt.show()