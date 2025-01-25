import math

number = float(input("Enter number of sides: "))

length = float(input("Enter length of a side: "))

area = ( number * ( length**2) ) / (4 * ( math.tan ( 3.142 / number) ) );

print(f"The area of the polygon is {area: .2f}");
