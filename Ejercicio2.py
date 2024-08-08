# Initialize the matrices
matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

# Function to add matrices
def add_matrices(matrix_A, matrix_B):
    result = [[a + b for a, b in zip(row_A, row_B)] for row_A, row_B in zip(matrix_A, matrix_B)]
    return result

# Function to subtract matrices
def subtract_matrices(matrix_A, matrix_B):
    result = [[a - b for a, b in zip(row_A, row_B)] for row_A, row_B in zip(matrix_A, matrix_B)]
    return result

# Function to compute the dot product of matrices
def dot_product(matrix_A, matrix_B):
    result = [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in zip(*matrix_B)] for row_A in matrix_A]
    return result

# Function to compute the cross product of matrices
def cross_product(matrix_A, matrix_B):
    result = [[matrix_A[1][0]*matrix_B[2][0] - matrix_A[2][0]*matrix_B[1][0],
               matrix_A[2][0]*matrix_B[0][0] - matrix_A[0][0]*matrix_B[2][0],
               matrix_A[0][0]*matrix_B[1][0] - matrix_A[1][0]*matrix_B[0][0]],
              [matrix_A[1][1]*matrix_B[2][1] - matrix_A[2][1]*matrix_B[1][1],
               matrix_A[2][1]*matrix_B[0][1] - matrix_A[0][1]*matrix_B[2][1],
               matrix_A[0][1]*matrix_B[1][1] - matrix_A[1][1]*matrix_B[0][1]],
              [matrix_A[1][2]*matrix_B[2][2] - matrix_A[2][2]*matrix_B[1][2],
               matrix_A[2][2]*matrix_B[0][2] - matrix_A[0][2]*matrix_B[2][2],
               matrix_A[0][2]*matrix_B[1][2] - matrix_A[1][2]*matrix_B[0][2]]]
    return result

# Function to divide matrices
def divide_matrices(matrix_A, matrix_B):
    result = [[a / b for a, b in zip(row_A, row_B)] for row_A, row_B in zip(matrix_A, matrix_B)]
    return result

# Perform the operations
print("Matrix addition:")
print(add_matrices(matrix_A, matrix_B))

print("\nMatrix subtraction:")
print(subtract_matrices(matrix_A, matrix_B))

print("\nDot product of matrices:")
print(dot_product(matrix_A, matrix_B))

print("\nCross product of matrices:")
print(cross_product(matrix_A, matrix_B))

print("\nMatrix division:")
print(divide_matrices(matrix_A, matrix_B))