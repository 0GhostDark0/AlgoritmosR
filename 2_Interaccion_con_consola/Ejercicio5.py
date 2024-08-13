#Select in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")

# code
def main():
    while True:
        response = input("Do you want to continue? Yes/No: ")
        response = response.strip().lower()

        if response == "yes":
            print("Continuing...")
        elif response == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid response. Try again.")

if __name__ == "__main__":
    main()