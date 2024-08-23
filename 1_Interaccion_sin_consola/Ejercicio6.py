# Double-acting cylinder in Python
# =======================

# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import library
import math

# Code
# Constants and input values
pressure_advance = 6  # Advance pressure (bar)
pressure_retract = 4  # Retract pressure (bar)
cylinder_diameter = 50  # Cylinder diameter (mm)
cylinder_length = 200  # Cylinder length (mm)
piston_rod_diameter = 20  # Piston rod diameter (mm)

# Calculate piston area and piston rod area
piston_area = math.pi * (cylinder_diameter/2)**2  # Piston area (mm²)
piston_rod_area = math.pi * (piston_rod_diameter/2)**2  # Piston rod area (mm²)

# Calculate advance force
advance_force = pressure_advance * (piston_area - piston_rod_area)
print("Advance force:", round(advance_force, 2), "N")

# Calculate retract force
retract_force = pressure_retract * (piston_area - piston_rod_area)
print("Retract force:", round(retract_force, 2), "N")