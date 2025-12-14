import numpy as np

marks = np.array([45, 60, 72, 81, 90, 55])

min=marks.min()
max=marks.max()
normalized=(marks-marks.min())/(marks.max()-marks.min())
print(normalized)
