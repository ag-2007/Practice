import matplotlib.pyplot as plt

Hours = [1,2,3,4,5,6,7,8]
Count = [200, 450, 900, 2000, 4200, 9000, 19500, 40000]

plt.plot(Hours, Count)
plt.yscale('log')
plt.xlabel('Hours')
plt.title("Hours vs Log(Count)")
plt.ylabel('Count (log scale)')
plt.show()