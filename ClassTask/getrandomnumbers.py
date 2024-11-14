import random
def get_randomnumber():
	response = 0
	failed = []
	correct = []
	positive_count= 0
	score  = 0
	counter = 0
	comparison= 0
	final_result = " "
	while counter < 10 :
		number1 = random.randrange(1, 1001)
		number2 = random.randrange(1, 1001)
	
		sign = ["+","+","+","+","+","*","*","*","-","-"]

		i = sign[counter]

		response = int(input(f" what will be the result of { number1 } {i} {number2} : =  "))
		if counter == 0:
			comparison = number1 + number2
		elif counter == 1:
			comparison = number1 + number2
		elif counter == 2:
			comparison = number1 + number2
		elif counter == 3:
			comparison = number1 + number2
		elif counter == 4:
			comparison = number1 + number2
		elif counter == 5:
			comparison = number1 * number2
		elif counter == 6:
			comparison = number1 * number2
		elif counter == 7:
			comparison = number1 * number2
		elif counter == 8:
			comparison = number1 - number2
		elif counter == 9:
			comparison = number1 - number2

		if response == comparison:
			correct.append(comparison)
			positive_count += 1
		else:
			final_result = f"You failed question  {counter+1 } The correct answer for {number1 } {sign[counter]}  {number2}  =   {comparison}"
			failed.append(final_result)


		counter+=1
	
	for i in failed:
		print(i)

	return f" {positive_count} / {counter} "

print(get_randomnumber())