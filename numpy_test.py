import numpy as np


# array of zeros

zeros_array = np.zeros(10)
print(zeros_array)

# array of fives
fives = np.array([5]* 10)
print("Five: ", fives)

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

 
 
 # Generate a random array of shape (3, 5) with values between 0 and 1
random_data = np.random.rand(3, 5)

print("Random Data:")
print(random_data)

# Calculate the mean of the random data along each axis
mean_axis_0 = np.mean(random_data, axis=0)
mean_axis_1 = np.mean(random_data, axis=1)

print("\nMean along axis 0:")
print(mean_axis_0)
print("\nMean along axis 1:")
print(mean_axis_1)

# Calculate the standard deviation of the random data along each axis
std_dev_axis_0 = np.std(random_data, axis=0)
std_dev_axis_1 = np.std(random_data, axis=1)

print("\nStandard Deviation along axis 0:")
print(std_dev_axis_0)
print("\nStandard Deviation along axis 1:")
print(std_dev_axis_1)

# Reshape the random data into a 1D array
reshaped_data = random_data.reshape(-1)

print("\nReshaped Data:")
print(reshaped_data)