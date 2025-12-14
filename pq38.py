import numpy as np

temp = np.array([
    [28, 30, 29, 31],
    [22, 24, 23, 25],
    [33, 35, 34, 36]
])

print(temp[1, 0:4])
print(temp[0:3, 2])
print(temp.mean(axis=1))
print(temp.mean(axis=0))
