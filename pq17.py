import pandas as pd 
import numpy as np

Name = ["Anika","Ravi","Meera","Kiran"]
Math = [88, 92, np.nan, 78]
Sci  = [91, 85, 79, np.nan]

data={"Name":Name, 
      "Math": Math, 
      "Sci":Sci
      }

df=pd.DataFrame(data)

math_mean=df['Math'].mean()
sci_mean=df['Sci'].mean()
df['Math']=df['Math'].fillna(math_mean)
df['Sci']=df['Sci'].fillna(sci_mean)
df['Total']=df['Math']+df['Sci']

result=[]

for i in df['Total']:
    if i>=160:
        result.append("Distinction")
    elif i>=140:
        result.append("First Class")
    else:
        result.append("Pass")

df['Result']=result

print(df[df['Result']=='Distinction'])