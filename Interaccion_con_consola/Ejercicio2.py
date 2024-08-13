#  Random Number Generator in Python
# =======================

# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import library
import random

# code
# Display a welcome message
print("Random Number Generator")

# Ask the user to enter the lower bound
lower_bound = int(input("Enter the lower bound: "))

# Ask the user to enter the upper bound
upper_bound = int(input("Enter the upper bound: "))

# Ask the user to enter the number of random numbers to generate
num_numbers = int(input("Enter the number of random numbers to generate: "))

# Generate the random numbers
random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(num_numbers)]

# Display the random numbers
print("The generated random numbers are:")
for i, number in enumerate(random_numbers):
    print(f"Number {i+1}: {number}")