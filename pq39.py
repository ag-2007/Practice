import numpy as np

sales = np.array([120, 150, 130, 180, 200, 220, 210])
mask = sales[1:]>sales[:-1]
increased=sales[1:][mask]
count=len(increased)