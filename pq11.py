import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Days  = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
Steps = [4500, 5600, 6200, 4800, 9000, 12000, 11000]

data={'Days':Days,
      'Steps': Steps}

df=pd.DataFrame(data)

df.plot(x='Days',y='Steps', kind='line', marker='o', title='Steps per day', grid=True)
max_steps=df['Steps'].max()
max_index=df['Steps'].idxmax()
max_day=df.loc[max_index, 'Days']
plt.scatter(max_index, max_steps, color='red', s=100, label='Highest Steps')
plt.show()