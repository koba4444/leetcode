import numpy as np

# Определите матрицы A и B
A = np.array([[3, 1, 0], [1, 2, 0], [5.,5.,5]])
B = np.array([9, 8, 0])

# Используйте функцию numpy.linalg.solve для решения уравнения A*X = B
X = np.linalg.solve(A, B)

print("Решение уравнения A*X = B:")
print(X)
