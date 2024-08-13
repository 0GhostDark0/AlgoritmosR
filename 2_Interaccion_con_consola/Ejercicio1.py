#  Power Calculator in Python
# =======================

# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import the input function to read user input
import math

# code
# Display a welcome message
print("Circuit Power Calculator")

# Ask the user to enter the current value (in amperes)
current = float(input("Enter the current value (in amperes): "))

# Ask the user to enter the voltage value (in volts)
voltage = float(input("Enter the voltage value (in volts): "))

# Calculate the power (in watts) using the formula P = V x I
power = voltage * current

# Display the result
print(f"The circuit power is: {power:.2f} watts")