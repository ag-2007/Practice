import numpy as np 

rev = np.array([
    [120, 135, 150, 160],   # Store A
    [100, 110, 130, 140],   # Store B
    [90,  95,  100, 120]    # Store C
])

print(rev[:, 1])
print(rev[2, :])
print(rev.sum())
print(rev.sum(axis=0))