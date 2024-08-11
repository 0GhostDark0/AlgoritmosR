#  double-acting cylinder in Python
# =======================

# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import the print function to display results
from builtins import print

# Display a welcome message
print("Power Calculator")

# Ask the user to input the current value
current = float(input("Enter the current value (A): "))

# Ask the user to input the voltage value
voltage = float(input("Enter the voltage value (V): "))

# Calculate the power
power = current * voltage

# Display the result
print("The power consumed by the circuit is:", round(power, 2), "W")