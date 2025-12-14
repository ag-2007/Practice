import matplotlib.pyplot as plt

Days   = list(range(1,11))
Usage  = [12,14,15,18,20,25,22,24,28,30]

plt.plot(Days, Usage)
plt.xlabel('Days')
plt.ylabel('Usage')
plt.title('Electricity Usage')

max_usage=max(Usage)
idx=Usage.index(max_usage)
day_max=Days[idx]

plt.scatter(day_max, max_usage, color='red', marker='o', label='Max Usage')

plt.show()
