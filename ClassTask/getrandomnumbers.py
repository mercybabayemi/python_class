import random
def get_randomnumber():
	response = 0
	failed = []
	correct_answer = []
	positive_count= 0
	negative_count= 0
	counter = 1
	while counter <= 10 :
		number1 = random.randrange(1,1001)
		number2 = random.randrange(1001)
				
		sign = ["+","+","+","+","+","*","*","*","-","-"]
		for  i in sign:
			response = input(f"{number1}{i}{number2}")
	counter+=1
	
	if response[i] == number1 + number2 :
		failed_numbers.append(number1)
	else:
		correct_answers.append(number1)
	
	print("Failed numbers are ", failed_numbers)
	print("Correct answers are ", correct_answers)
