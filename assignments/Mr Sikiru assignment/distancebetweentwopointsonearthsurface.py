import math

x1 = float(input("Input the latitude of coordinate 1: "))
 
y1 = float(input("Input the longitude of coordinate 1: "))

x2 = float(input("Input the latitude of coordinate 2: "))
 
y2 = float(input("Input the longitude of coordinate 2: "))

radius = 6371.01

rx1 = math.radians(x1)
rx2 = math.radians(x2)
ry1 = math.radians(y1)
ry2 = math.radians(y2)


distance = radius * math.acos ((math.sin(rx1)) * math.sin(rx2) + math.cos(rx1) *
math.cos(rx2) * math.cos(ry1 - ry2))

print(f"The distance between those points is: {distance:.2f}")
