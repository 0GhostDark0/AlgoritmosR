#Transfer function in Python
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
def plot_transfer_function(a, b, c, d):
    # Create the second-order transfer function
    num = [a, b]
    den = [1, c, d]
    sys = tf2ss(num, den)

    # Plot the frequency response
    w, mag, phase = lti(*sys).bode()
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(w, mag)
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Magnitude (dB)')

    discriminant = c**2 - 4*d
    if discriminant > 0:
        title = "Overdamped System Frequency Response"
    elif discriminant == 0:
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
    if discriminant > 0:
        print("The system is overdamped.")
    elif discriminant == 0:
        print("The system is critically damped.")
    else:
        print("The system is underdamped.")

# Ask the user to input the coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = float(input("Enter coefficient d: "))

# Plot the transfer function
plot_transfer_function(a, b, c, d)