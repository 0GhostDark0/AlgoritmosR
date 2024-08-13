#Temperature in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")


# Import library
import numpy as np
import matplotlib.pyplot as plt

# code
# Define the temperature range
temperatures = np.linspace(-200, 200, 400)

# Define the PT100 resistance function
def pt100_resistance(t):
    return 100 * (1 + 0.00385 * t)

# Calculate the resistance for each temperature
resistances = [pt100_resistance(t) for t in temperatures]

# Create the plot
plt.plot(temperatures, resistances)
plt.xlabel('Temperature (°C)')
plt.ylabel('Resistance (Ω)')
plt.title('PT100 Sensor Behavior')
plt.grid(True)
plt.show()

