from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

Speed = np.array([20, 40, 60, 80, 100])
Mileage = np.array([22, 24, 20, 17, 14])

f=interp1d(Speed, Mileage, kind='quadratic')

x_new=np.linspace(20, 100, 160)
y_new=f(x_new)

print("=====Original Data Points=====")
for xi, yi in zip(Speed, Mileage):
    print(f"{xi:.2f}, {yi:.2f} ")

print("=====New Data Points=====")
for xi, yi in zip(x_new, y_new):
    print(f"{xi:.2f}, {yi:.2f} ")

plt.scatter(Speed, Mileage, color='red', label='Original Data Points')
plt.plot(x_new, y_new, color='g', label='Interpolate Mileage')
plt.scatter(70, f(70), color='blue', label='Estimated speed at 70 km/h')
plt.xlabel('Speed')
plt.ylabel('Mileage')
plt.title("Fuel Efficiency Curve")
plt.legend()
plt.show()