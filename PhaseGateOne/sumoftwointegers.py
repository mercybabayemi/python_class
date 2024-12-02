"""
Pseudocode for sum of integer
- prompt user for the first integer
- collect and save as first_integer
- prompt user for the second integer 
- collect and save as second integer 
- prompt the user to enter the sum of these integers 
- if sum of integer input is correct, answer is true or false if otherwise.
"""

first_integer = int(input("Enter first integer: "))
second_integer = int(input("Enter second integer: "))

total = int(input(f"Enter the sum total of {first_integer}+{second_integer}: "))

def get_sum(first_integer,second_integer):
	result = first_integer + second_integer
	return result

my_sum = get_sum(first_integer,second_integer)

if my_sum == total:
	answer = True
else:
	answer = False

print(answer)
