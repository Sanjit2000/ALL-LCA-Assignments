# Write a program create an array and perform addition of two matrices using nested loops. Display the final result after performing the addition operation.

import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])

# Perform addition using nested loops
result = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Display the final result
print("Result of matrix addition:")
print(result)