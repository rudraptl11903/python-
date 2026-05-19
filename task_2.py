# Program to calculate volume and surface area of a cylinder

import math

# Taking input from user
radius = float(input("Enter radius : "))
height = float(input("Enter height : "))

# Calculations
volume = 3.14 * radius * radius * height
surface_area = (2 * 3.14 * radius * radius) + (2 * 3.14* radius * height)


print("\nVolume of Cylinder =", round(volume, 2))
print("Surface Area of Cylinder =", round(surface_area, 2))