import pandas as pd
import numpy as np

Day  = [1,2,3,4,5,6]
Temp = [98.6, 99.1, np.nan, 100.2, np.nan, 99.5]

data={'Day':Day, 
      "Temp":Temp}

df=pd.DataFrame(data)
mean_temp=df['Temp'].mean()
df['Temp']=df['Temp'].fillna(mean_temp)

high=0
low=0
status=[]

for i in df['Temp']:
    if i>99.5:
        status.append("High")
        high+=1
    else:
        status.append("Normal")
        low+=1

df['Status']=status
print(df)
print("High:", high)
print("Low", low)

df.to_excel("temperature.xlsx", index='False')