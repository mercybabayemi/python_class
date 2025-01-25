first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

largest_number = 0
smallest_number = 0
answer = 0

if first_number > second_number:
	largest_number = first_number
	smallest_number = second_number

else: 
	largest_number = second_number
	smallest_number = first_number

while True:
	
	user_input = int(input("Enter number(-1 to exit): "))

	if user_input == -1:
		break

	if user_input > largest_number:
		largest_number = user_input

	elif user_input < largest_number:
		smallest_number = user_input


	print("Largest Number is ", largest_number)
	print("Smallest Number is ", smallest_number)	

print("Final Largest Number is ", largest_number)
print("Final Smallest Number is ", smallest_number)	

