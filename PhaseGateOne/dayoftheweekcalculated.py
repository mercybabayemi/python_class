"""
pseudocode today's day of the week 
- Prompt user to enter an integer for todays date 
- collect and store response as option
- prompt user to enter the numbers of days after today for a future date and display the future day of the week
"""
	

message = """ 
	What is today's day?
	Enter 0 for Sunday
	Enter 1 for Monday
	Enter 2 for Tuesday
	Enter 3 for Wednesday
	Enter 4 for Thursday
	Enter 5 for Friday
	Enter 6 for Saturday
	"""
todays_day =" "
	
option = int(input(message))
	
match option: 
	case 0:
		todays_date = "Sunday"
		print(f"Today is {todays_date}.")
	case 1:
		todays_date = "Monday"
		print(f"Today is {todays_date}.")
	case 2: 
		todays_date = "Tuesday"
		print(f"Today is {todays_date}.")
	case 3:
		todays_date = "Wednesday"
		print(f"Today is {todays_date}.")
	case 4:
		todays_date = "Thursday"
		print(f"Today is {todays_date}.")
	case 5:
		todays_date = "Friday"
		print(f"Today is {todays_date}.")
	case 6:
		todays_date = "Saturday"
		print(f"Today is {todays_date}.")
	case _:
			print("Default, enter the right value!!")
			get_day()

def get_calculation(option,todays_date):
	message = """ 
		What is the future day?
		Enter numerical value: 
		"""
	days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
	new_input = (input(message))

	for index at range(new_input):
		future_day += days[index]

		

get_calculation(option,todays_date)