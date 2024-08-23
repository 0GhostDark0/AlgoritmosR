# Transfer function in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import library
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2ss, lti

# code
def plot_transfer_function(wn, zeta):
    # Create the second-order transfer function
    num = [wn**2]
    den = [1, 2*zeta*wn, wn**2]
    sys = tf2ss(num, den)

    # Plot the frequency response
    w, mag, phase = lti(*sys).bode()
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(w, mag)
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Magnitude (dB)')

    if zeta > 1:
        title = "Overdamped System Frequency Response"
    elif zeta == 1:
        title = "Critically Damped System Frequency Response"
    else:
        title = "Underdamped System Frequency Response"
    plt.title(title)

    plt.subplot(2, 1, 2)
    plt.plot(w, phase)
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Phase (degrees)')
    plt.title('Phase Response')

    plt.tight_layout()
    plt.show()

    # Determine the system type
    if zeta > 1:
        print("The system is overdamped.")
    elif zeta == 1:
        print("The system is critically damped.")
    else:
        print("The system is underdamped.")

# Ask the user to input the coefficients
wn = float(input("Enter natural frequency (wn): "))
zeta = float(input("Enter damping ratio (zeta): "))

# Plot the transfer function
plot_transfer_function(wn, zeta)