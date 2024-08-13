#image reading in Python
# =======================
# Initialize date and time
import datetime
print(f"**User:** Alejandro")
print(f"**Date and Time:** {datetime.datetime.now()}")
# Import library
import cv2
import numpy as np

# code
# Load the images mazda
mazda_logo = cv2.imread('C:\\Users\\ALEJANDRO\\Desktop\\Algoritmos_R\\Funciones_para_graficar\\Logos\\mazda.png')

# Load the images mercedes
mercedes_logo = cv2.imread('C:\\Users\\ALEJANDRO\\Desktop\\Algoritmos_R\\Funciones_para_graficar\\Logos\\mercedes.png')

# Convert the images to grayscale
mazda_gray = cv2.cvtColor(mazda_logo, cv2.COLOR_BGR2GRAY)
mercedes_gray = cv2.cvtColor(mercedes_logo, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, mazda_thresh = cv2.threshold(mazda_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
_, mercedes_thresh = cv2.threshold(mercedes_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours
contours_mazda, _ = cv2.findContours(mazda_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_mercedes, _ = cv2.findContours(mercedes_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the X and Y coordinates of the contours
mazda_contour = contours_mazda[0]
mercedes_contour = contours_mercedes[0]

mazda_x = mazda_contour[:, 0, 0]
mazda_y = mazda_contour[:, 0, 1]

mercedes_x = mercedes_contour[:, 0, 0]
mercedes_y = mercedes_contour[:, 0, 1]

print("Mazda Contour X:", mazda_x)
print("Mazda Contour Y:", mazda_y)

print("Mercedes Contour X:", mercedes_x)
print("Mercedes Contour Y:", mercedes_y)