import numpy as np

battery = np.array([95, 90, 88, 50, 40, 20, 10, 8, 15, 30])

mask=battery<20
battery_copy=battery
battery_copy[mask]=20
count=mask.sum()
