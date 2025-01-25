
first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))



if first_number > second_number and second_number > third_number:
	print("Number is in desending order")
elif first_number < second_number and second_number < third_number:
	print("Number is in ascending order")
else:
	print("Number has no order")

