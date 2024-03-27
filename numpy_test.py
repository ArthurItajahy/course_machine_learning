import numpy as np

# Create a 3x3 matrix filled with zeros
matrix = np.zeros((3, 3))

print("Original Matrix:")
print(matrix)

# Fill the matrix with some values
for i in range(3):
    for j in range(3):
        matrix[i][j] = i + j

print("\nMatrix after filling with values:")
print(matrix)

# Transpose the matrix
transposed_matrix = np.transpose(matrix)

print("\nTransposed Matrix:")
print(transposed_matrix)

# Find the determinant of the matrix
determinant = np.linalg.det(matrix)

print("\nDeterminant of the Matrix:", determinant)

# Find the inverse of the matrix
if determinant != 0:
    inverse_matrix = np.linalg.inv(matrix)
    print("\nInverse of the Matrix:")
    print(inverse_matrix)
else:
    print("\nThe matrix is singular, so its inverse cannot be computed.")