import numpy as np
import pandas as pd

data = np.array([2.4, 3.1, np.nan, 4.5, np.nan, 5.2])

data=pd.Series(data)

data=data.fillna(data.mean())
print(data)