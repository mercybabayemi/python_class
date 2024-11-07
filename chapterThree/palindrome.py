integer = int(input('Enter a five digit integer: '))

for number in range(1):
	first_number = integer // 10000

	second_trial = integer // 1000
	second_number = second_trial % 10

	third_trial = integer // 100
	third_number = third_trial % 10

	fourth_trial = integer // 10
	fourth_number = fourth_trial % 10

	fifth_number = integer % 10

	if first_number == fifth_number and second_number == fourth_number:
		print('Number is a palindrome')
	else:
		print('Number is not a palindrome')