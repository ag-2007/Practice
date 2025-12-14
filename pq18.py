import pandas as pd
import numpy as np

Items   = ["Milk","Bread","Eggs","Juice","Butter"]
Price   = [40, 30, np.nan, 50, 60]
Stock   = [10, np.nan, 30, 20, np.nan]

data={'Items':Items, 
      'Price':Price,
      'Stock':Stock}

df=pd.DataFrame(data)
df_clean=df.dropna(subset=['Price','Stock'], how="all")
mean_price=df['Price'].mean()
median_stock=df['Stock'].median()
df['Price']=df['Price'].fillna(mean_price)
df['Stock']=df['Stock'].fillna(median_stock)
df['Value']=df['Price']*df['Stock']
print(df)
print()
print("This is the item with highest inventory value")
print(df['Value'].max())
print()
print("The totalvalue of all stock is:")
print(df["Value"].sum())


