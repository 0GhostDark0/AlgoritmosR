#Calculate the charging and discharging voltage in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")


# Import library
import matplotlib.pyplot as plt
import numpy as np

#code
# Get input values from the user
V = float(input("Enter the voltage (V): "))
C = float(input("Enter the capacitance (μF): "))
R = float(input("Enter the resistance (Ω): "))

# Calculate the time constant
tau = R * C * 1e-6

# Create a time array
t = np.linspace(0, 5 * tau, 1000)

# Calculate the charging and discharging voltage
Vc_charge = V * (1 - np.exp(-t / tau))
Vc_discharge = V * np.exp(-t / tau)

# Plot the results
plt.figure(figsize=(10, 4))

# Charging graph
plt.subplot(1, 2, 1)
plt.plot(t, Vc_charge, 'b-', label='Charging')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Capacitor Charging')
plt.grid(True)

# Discharging graph
plt.subplot(1, 2, 2)
plt.plot(t, Vc_discharge, 'b-', label='Discharging')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Capacitor Discharging')
plt.grid(True)

plt.tight_layout()
plt.show()