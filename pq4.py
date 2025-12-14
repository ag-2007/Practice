usage = [120, 135, 150, 142, 138, 160, 170, 175, 180, 190]

import numpy as np
import matplotlib.pyplot as plt

Usage=np.array(usage)
avg_consumption=np.mean(Usage)

percentage_increase=(Usage[1:] - Usage[:-1]) / Usage[:-1] * 100 

import matplotlib.pyplot as plt

days = np.arange(1, len(usage) + 1)

fig, ax1 = plt.subplots()

# Plot daily usage (left y-axis)
ax1.plot(days, usage, 'b-o', label='Daily Usage (kWh)')
ax1.set_xlabel('Day')
ax1.set_ylabel('Power Usage (kWh)', color='b')

# Create right y-axis
ax2 = ax1.twinx()

# Plot percentage change (right y-axis)
ax2.plot(days[1:], percentage_increase, 'r--s', label='Daily % Increase')
ax2.set_ylabel('Percentage Change (%)', color='r')

# Add title and grid
plt.title('Power Consumption Trend Over 10 Days')
ax1.grid(True, linestyle='--', alpha=0.6)

# Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()


