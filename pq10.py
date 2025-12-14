import pandas as pd
import matplotlib.pyplot as plt

Products = ["Laptop","Tablet","Headphones","Camera"]
Sales    = [40, 55, 120, 30]

data={'Products': Products,
      'Sales':Sales}

df=pd.DataFrame(data)

print(f"The product should promote the following more based on demand")
print(df.max())
df.plot(x='Products', y='Sales', kind='bar', title='Products and Sales')
plt.xlabel('Products')
plt.ylabel('Sales')

for index, value in enumerate(df['Sales']):
    plt.text(index, value+2, str(value), ha='center')

plt.show()
