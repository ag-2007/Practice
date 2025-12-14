steps = [4000, 5600, 6200, 4500, 8000, 10000, 9500, 7200, 6800, 7900, 8300, 9100, 10200, 8900]
Days=list(range(1, len(steps)+1))

import pandas as pd

df = pd.DataFrame({'Day': Days, 'Steps': steps})
total_steps=df['Steps'].sum()
avg_steps=df['Steps'].mean()

print(f'Total Steps in 14 days: {total_steps}')
print(f'Average Daily Steps: {avg_steps:.2f}')

mask=df['Steps']<avg_steps
below_avg=df[mask]

import matplotlib.pyplot as plt

colors = ['red' if s < avg_steps else 'green' for s in df['Steps']]

plt.figure(figsize=(8,5))
plt.plot(df['Day'], df['Steps'], 'k--', alpha=0.6)   # thin dashed baseline
plt.scatter(df['Day'], df['Steps'], c=colors, s=80, edgecolor='black')

plt.axhline(avg_steps, color='blue', linestyle='--', label=f'Average = {avg_steps:.0f}')

plt.title('Daily Step Count (14 Days)')
plt.xlabel('Day')
plt.ylabel('Steps Count')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()
