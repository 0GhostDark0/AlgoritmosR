# Temperature in Python
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

# Define the PT100 resistance function using Callendar-Van Dusen equations
def pt100_resistance(t):
    if t >= 0:
        # Callendar-Van Dusen equation for positive temperatures
        return 100 * (1 + 3.9083e-3 * t - 5.775e-7 * t**2 - 4.183e-12 * t**3)
    else:
        # Callendar-Van Dusen equation for negative temperatures
        return 100 * (1 + 3.9083e-3 * t - 5.775e-7 * t**2 - 4.183e-12 * t**3 + 1.235e-15 * t**4)

# Calculate the resistance for each temperature
resistances = [pt100_resistance(t) for t in temperatures]

# Create the plot
plt.plot(temperatures, resistances)
plt.xlabel('Temperature (°C)')
plt.ylabel('Resistance (Ω)')
plt.title('PT100 Sensor Behavior')
plt.grid(True)
plt.show()