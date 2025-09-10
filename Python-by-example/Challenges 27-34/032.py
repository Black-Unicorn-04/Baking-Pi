import math

radius = float(input("Enter the radius of a cylinder: "))

depth = float(input("Enter the depth of a cylinder: "))

total_volume = math.pi*(radius**2)*depth

print(round(total_volume,3))