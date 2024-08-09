# Rotations in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import library
import numpy as np

# Code
def rotation_x(angle):
    """
    Rotation around X axis.

    Parameters:
    angle (float): Rotation angle in radians.

    Returns:
    matrix (numpy array): 3x3 rotation matrix.
    """
    matrix = np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])
    return matrix

def rotation_y(angle):
    """
    Rotation around Y axis.

    Parameters:
    angle (float): Rotation angle in radians.

    Returns:
    matrix (numpy array): 3x3 rotation matrix.
    """
    matrix = np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])
    return matrix

def rotation_z(angle):
    """
    Rotation around Z axis.

    Parameters:
    angle (float): Rotation angle in radians.

    Returns:
    matrix (numpy array): 3x3 rotation matrix.
    """
    matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    return matrix

# Example usage
angle_x = np.pi / 2  # 90 degrees in radians
matrix_x = rotation_x(angle_x)
print("Rotation around X axis:")
print(matrix_x)

angle_y = np.pi / 4  # 45 degrees in radians
matrix_y = rotation_y(angle_y)
print("\nRotation around Y axis:")
print(matrix_y)

angle_z = np.pi / 3  # 60 degrees in radians
matrix_z = rotation_z(angle_z)
print("\nRotation around Z axis:")
print(matrix_z)