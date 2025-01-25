"""
pseudocode of three integers in increasing order
- declare an empty list
- prompt user to enter first integer
- collect and save it as first_integer
- append to empty list
- prompt user to enter second integer
- collect and store it as integer
- append to empty list
- prompt user to enter third integer
- append to empty list
- sort list 
-display result
"""

numbers = []
first_integer = int(input("Enter first integer: "))
numbers.append(first_integer)
second_integer = int(input("Enter second integer: "))
numbers.append(second_integer)
third_integer = int(input("Enter third integer: "))
numbers.append(third_integer)

print(sorted(numbers))

