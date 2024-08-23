# Draw Letters in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import libraries
import matplotlib.pyplot as plt

# Define letter coordinates
# ------------------------
# Coordinates for each letter
letters = {
    'J': [(0, 4), (2, 4), (2, 3), (1, 3), (1, 0), (0, 0)],
    'U': [(0, 4), (0, 1), (1, 0), (2, 1), (2, 4)],
    'A': [(0, 0), (1, 4), (2, 0), (1, 2), (0, 2), (2, 2)], 
    'N': [(0, 0), (0, 4), (2, 0), (2, 4)],
    'L': [(0, 4), (0, 0), (2, 0)],
    'E': [(0, 4), (2, 4), (0, 4), (0, 2), (2, 2), (0, 2), (0, 0), (2, 0)],
    'O': [(0, 4), (2, 4), (2, 0), (0, 0), (0, 4)],
    'S': [(2, 4), (0, 4), (0, 2), (2, 2), (2, 0), (0, 0)],
    'B': [(0, 0), (0, 4), (2, 3), (0, 2), (2, 1), (0, 0)],
}

# Define word offsets
# -------------------
# Offset for each word
offsets = {
    'JUAN': (0, 10),
    'ALEJO': (0, 5),
    'SEBAS': (0, 0),
}

# Create plot
# -----------
# Create the figure and axis
fig, ax = plt.subplots()

# Draw letters
# ------------
# Draw the letters of each word
for word, (x_offset, y_offset) in offsets.items():
    x_shift = x_offset
    for letter in word:
        # Get the coordinates of the letter
        coords = letters[letter]
        x_coords = [x + x_shift for x, y in coords]
        y_coords = [y + y_offset for x, y in coords]
        
        # Draw the lines of the letter
        ax.plot(x_coords, y_coords, color='black', linewidth=5)
        
        # Move to the next letter
        x_shift += 3

# Configure plot
# --------------
# Configure the axis (show the Cartesian plane)
ax.set_xlim(-2, 18)
ax.set_ylim(-2, 15)
ax.grid(True)  # Show the Cartesian plane
ax.set_aspect('equal')  # Maintain aspect ratio

# Set title
# ----------
# Set the title of the plot
plt.title("Group Members:")

# Show plot
# ---------
# Show the graph
plt.show()