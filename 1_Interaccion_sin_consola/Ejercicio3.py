# Coordinates in Python
# =======================

# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import library
import math


# Code
def rectangular_to_cylindrical(x, y, z):
    """
    Converts rectangular coordinates to cylindrical coordinates.
    
    Args:
        x (float): Rectangular x coordinate.
        y (float): Rectangular y coordinate.
        z (float): Rectangular z coordinate.
    
    Returns:
        tuple: Cylindrical coordinates (r, theta, z).
    """
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta, z

def rectangular_to_spherical(x, y, z):
    """
    Converts rectangular coordinates to spherical coordinates.
    
    Args:
        x (float): Rectangular x coordinate.
        y (float): Rectangular y coordinate.
        z (float): Rectangular z coordinate.
    
    Returns:
        tuple: Spherical coordinates (rho, theta, phi).
    """
    rho = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / rho)
    return rho, theta, phi

# Example usage
x, y, z = 1, 2, 3
r, theta, z_cylindrical = rectangular_to_cylindrical(x, y, z)
rho, theta_spherical, phi = rectangular_to_spherical(x, y, z)

print("Rectangular coordinates:", x, y, z)
print("Cylindrical coordinates:", r, theta, z_cylindrical)
print("Spherical coordinates:", rho, theta_spherical, phi)