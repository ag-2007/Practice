Orders = [2400, 1500, 3150, 800, 2700, 5000, 3200, 450, 900]
Categories = ['Electronics', 'Books', 'Clothing', 'Books', 'Electronics', 'Electronics', 'Clothing', 'Books', 'Clothing']

data={'Orders':Orders, 
      'Categories':Categories
      }

import pandas as pd

df=pd.DataFrame(data)

avg_ordervalue=df['Orders'].mean()
min_order=df['Orders'].min()
max_order=df['Orders'].max()

discounted=[]

for i in range(len(df)):
    value=df.loc[i, 'Orders']

    if value>3000:
        discount=value*0.90
    else:
        discount=value*0.95
    discounted.append(discount)

df['Discounted']=discounted

print(df)

category_revenue = df.groupby('Categories')['Discounted'].sum()
print(category_revenue)

