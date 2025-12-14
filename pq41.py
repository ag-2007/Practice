import numpy as np

A = np.array([
    [2, 3],
    [4, 1]
])

B = np.array([[1,2],[0,1]])

print(np.linalg.det(A))
print(A.T)
print(A.dot(B))
print(np.linalg.det(A.dot(B)))