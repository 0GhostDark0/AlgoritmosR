# Draw vector in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import library
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# code
def plot_vector(x, y, z):
    fig = plt.figure(figsize=(10, 8))  # Increase figure size
    ax = fig.add_subplot(111, projection='3d')

    # Draw axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Draw vector with thinner arrow
    ax.quiver(0, 0, 0, x, y, z, color='r', length=1, linewidth=0.5)

    # Set axis limits based on the input values
    max_val = max(abs(x), abs(y), abs(z))
    ax.set_xlim(-max_val*1.1, max_val*1.1)
    ax.set_ylim(-max_val*1.1, max_val*1.1)
    ax.set_zlim(-max_val*1.1, max_val*1.1)

    plt.show()

# Ask user to input vector coordinates
x_coord = float(input("Enter the X coordinate of the vector: "))
y_coord = float(input("Enter the Y coordinate of the vector: "))
z_coord = float(input("Enter the Z coordinate of the vector: "))

# Plot the vector
plot_vector(x_coord, y_coord, z_coord)