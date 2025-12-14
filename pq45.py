import numpy as np

img = np.array([
[120, 130, 140],
[150, 160, 170],
[180, 190, 200]
])

new_img=img+20
print(new_img)
print(new_img[1, :])
print(new_img[:,0])
print(new_img.mean())