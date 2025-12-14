import pandas as pd
import matplotlib.pyplot as plt

Month   = ["Jan","Feb","Mar","Apr","May","Jun"]
Revenue = [120000, 135000, 128000, 140000, 150000, 170000]

data={'Month': Month,
      'Revenue': Revenue}
df=pd.DataFrame(data)
print(df.max())
df.plot(x='Month', y='Revenue',kind='line', marker='o', color='red', title='Month and Revenue', grid=True )
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.show()