import pandas as pd

df=pd.read_csv("products.csv")
print(df)
print(df.isnull())
average_stock=df['Stock'].mean()
df['Stock']=df['Stock'].fillna(average_stock)
df['TotalValue']=df['Price']*df['Stock']
print()
print(df)

df.to_csv('products_cleaned.csv', index='False')
