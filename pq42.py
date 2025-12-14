import numpy as np

hr = np.array([78, 80, 82, 85, 90, 88, 84, 79, 76, 74, 72])

print(hr[0:4])
print(hr[-3:])
print(hr[::2])
mask=hr>85
print(len(hr[mask]))