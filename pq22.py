import matplotlib.pyplot as plt

Height = [150, 160, 165, 170, 175, 180]
Weight = [50, 60, 63, 70, 75, 80]
Age    = [20, 25, 28, 32, 40, 45]

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

ax.scatter(Height, Weight, Age)

ax.set_xlabel("Height (cm)")
ax.set_ylabel("Weight (kg)")
ax.set_zlabel("Age (years)")

plt.title("3D Scatter Plot: Height vs Weight vs Age")
plt.show()