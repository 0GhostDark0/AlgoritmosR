# Reading Image Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")
# Import library
import cv2
import numpy as np

# Code
# Load logo images
mazda_logo = cv2.imread('C:\\Users\\ALEJANDRO\\Desktop\\Algoritmos_R\\3_Funciones_para_graficar\\Logos\\mazda.png')
mercedes_logo = cv2.imread('C:\\Users\\ALEJANDRO\\Desktop\\Algoritmos_R\\3_Funciones_para_graficar\\Logos\\mercedes.png')

# Check if images loaded correctly
if mazda_logo is None:
    print("Error: Could not load Mazda image")
if mercedes_logo is None:
    print("Error: Could not load Mercedes image")

# Binarize images to detect contours
imgCanny_mazda = cv2.Canny(mazda_logo, 50, 150)  # Adjust Canny parameters for Mazda
imgCanny_mercedes = cv2.Canny(mercedes_logo, 10, 50)

# Find contours of images
contours_mazda, hierarchy_mazda = cv2.findContours(imgCanny_mazda, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_mercedes, hierarchy_mercedes = cv2.findContours(imgCanny_mercedes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Print contour coordinates
print("Coordinates of Mazda contours:")
for contour in contours_mazda:
    for point in contour:
        x, y = point[0]
        print(f"({x}, {y})")

print("\nCoordinates of Mercedes contours:")
for contour in contours_mercedes:
    for point in contour:
        x, y = point[0]
        print(f"({x}, {y})")

# Draw found contours
cv2.drawContours(mazda_logo, contours_mazda, -1, (0,255,0), 3)
cv2.drawContours(mercedes_logo, contours_mercedes, -1, (0,255,0), 3)

# Display images with drawn contours
cv2.imshow("Mazda Image", mazda_logo)
cv2.imshow("Mercedes Image", mercedes_logo)
cv2.waitKey(0)
cv2.destroyAllWindows()