"""
pseudocode today's day of the week 
- Declare days of the week
- Prompt user to enter an integer for todays date 
- collect and store response as option
- prompt user to enter the numbers of days after today for a future date and display the future day of the week
"""

def get_calculation():
	days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	
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
	option = int(input(message))

	new_input = int(input("What is the future day?\nHow many days from today?"))
	future_day_index = (option + new_input) % 7
	future_day = days[future_day_index]

	print(f"The future day is {future_day}")
		

get_calculation()