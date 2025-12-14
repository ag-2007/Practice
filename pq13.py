import pandas as pd 
import matplotlib.pyplot as plt

Day   = [1,2,3,4,5,6,7]
Temp  = [28.5, 29.0, 31.2, 33.1, 35.0, 34.5, 32.0]

data = {'Day': Day, 
        'Temp': Temp}

df=pd.DataFrame(data)

df.plot(x='Day', y='Temp', title='Temperature Trends')
plt.fill_between(df['Day'], df['Temp'], alpha=0.3)
plt.xlabel('Day')
plt.ylabel('Temp')
plt.show()