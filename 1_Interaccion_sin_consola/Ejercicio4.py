# Resistance of a Platinum RTD (PT100) in Python
# =======================

# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Code
def calculate_resistance(temperature):
    """
    Calculates the resistance of a Platinum RTD (PT100) based on the temperature.

    Parameters:
    temperature (float): Temperature in degrees Celsius.

    Returns:
    float: Resistance in ohms.
    """
    # Coefficients for the Callendar-Van Dusen equation (positive temperatures)
    a = 3.9083e-3
    b = -5.775e-7
    c = -4.183e-12

    # Coefficients for the Callendar-Van Dusen equation (negative temperatures)
    a_neg = 3.9083e-3
    b_neg = -5.775e-7
    c_neg = -4.183e-12
    d_neg = 1.235e-15

    if temperature >= 0:
        # Callendar-Van Dusen equation for positive temperatures
        resistance = 100 * (1 + a * temperature + b * temperature**2 + c * temperature**3)
    else:
        # Callendar-Van Dusen equation for negative temperatures
        resistance = 100 * (1 + a_neg * temperature + b_neg * temperature**2 + c_neg * temperature**3 + d_neg * temperature**4)

    return resistance

# Test temperature (in degrees Celsius)
test_temperature = 25

# Calculate the resistance
resistance = calculate_resistance(test_temperature)

# Print the result
print(f"The resistance of the Platinum RTD (PT100) at {test_temperature}°C is {resistance:.2f} ohms")