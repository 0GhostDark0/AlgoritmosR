#Draw vector in Python
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
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Draw vector with thinner arrow
    ax.quiver(0, 0, 0, x, y, z, color='r', length=1, linewidth=0.5)

    # Set axis limits
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

    plt.show()

# Ask user to input vector coordinates
x_coord = float(input("Enter the X coordinate of the vector: "))
y_coord = float(input("Enter the Y coordinate of the vector: "))
z_coord = float(input("Enter the Z coordinate of the vector: "))

# Plot the vector
plot_vector(x_coord, y_coord, z_coord)