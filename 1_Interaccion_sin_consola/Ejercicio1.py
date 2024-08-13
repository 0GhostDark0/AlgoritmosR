# Vectors in Python
# =======================

# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Code
# Initialize two vectors
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]

# Vector addition
sum_vector = [a + b for a, b in zip(vector_a, vector_b)]
print("Vector sum:", sum_vector)

# Vector subtraction
difference_vector = [a - b for a, b in zip(vector_a, vector_b)]
print("Vector difference:", difference_vector)

# Dot product of vectors
dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
print("Dot product:", dot_product)

# Cross product of vectors 
def cross_product(vector_a, vector_b):
    return [vector_a[1]*vector_b[2] - vector_a[2]*vector_b[1],
            vector_a[2]*vector_b[0] - vector_a[0]*vector_b[2],
            vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]]

cross_product_vector = cross_product(vector_a, vector_b)
print("Cross product:", cross_product_vector)

# Vector division (cannot divide by zero)
division_vector = [a / b for a, b in zip(vector_a, vector_b) if b != 0]
print("Vector division:", division_vector)