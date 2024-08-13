#Articulations  in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# code
def display_robot_info(robot_type):
    if robot_type == "Spherical":
        print(f"Robot {robot_type} has {4} articulations.")
    elif robot_type == "Cartesian":
        print(f"Robot {robot_type} has {3} articulations.")
    elif robot_type == "Cylindrical":
        print(f"Robot {robot_type} has {3} articulations.")
    else:
        print("Invalid robot type")

def main():
    print("Select a robot type:")
    print("1. Spherical")
    print("2. Cartesian")
    print("3. Cylindrical")
    option = int(input("Enter the option: "))

    if option == 1:
        robot_type = "Spherical"
    elif option == 2:
        robot_type = "Cartesian"
    elif option == 3:
        robot_type = "Cylindrical"
    else:
        print("Invalid option")
        return

    display_robot_info(robot_type)

if __name__ == "__main__":
    main()