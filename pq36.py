import numpy as np 

steps = np.array([4000, 5600, 6200, 4500, 8000, 10000, 9500])

average=steps.mean()
print("Average steps =", average)

mask=steps>average

above_avg=steps[mask]
print("Steps above average:", above_avg)

percentage = (mask.sum() / len(steps)) * 100
print("Percentage of days above average =", percentage, "%")
