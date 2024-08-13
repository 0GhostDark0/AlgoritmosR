# Volume Calculator in Python
# =======================

# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# Import library
import math

# code
def calculate_prism_volume(base, height):
    return base * height

def calculate_pyramid_volume(base, height):
    return (base ** 2) * height / 3

def calculate_truncated_cone_volume(radius1, radius2, height):
    return math.pi * (radius1 ** 2 + radius2 ** 2 + radius1 * radius2) * height / 3

def calculate_cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

def main():
    print("Volume Calculator")
    print("1. Prism")
    print("2. Pyramid")
    print("3. Truncated Cone")
    print("4. Cylinder")
    option = int(input("Select the solid: "))

    if option == 1:
        base = float(input("Enter the base of the prism: "))
        height = float(input("Enter the height of the prism: "))
        volume = calculate_prism_volume(base, height)
        print(f"The volume of the prism is: {volume:.2f} cubic units")
    elif option == 2:
        base = float(input("Enter the base of the pyramid: "))
        height = float(input("Enter the height of the pyramid: "))
        volume = calculate_pyramid_volume(base, height)
        print(f"The volume of the pyramid is: {volume:.2f} cubic units")
    elif option == 3:
        radius1 = float(input("Enter radius 1 of the truncated cone: "))
        radius2 = float(input("Enter radius 2 of the truncated cone: "))
        height = float(input("Enter the height of the truncated cone: "))
        volume = calculate_truncated_cone_volume(radius1, radius2, height)
        print(f"The volume of the truncated cone is: {volume:.2f} cubic units")
    elif option == 4:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        volume = calculate_cylinder_volume(radius, height)
        print(f"The volume of the cylinder is: {volume:.2f} cubic units")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()