from datetime import datetime, timedelta
def get_welcome_message():
	print("Welcome to your ultimate menstrual calculator>>>\n")

def get_user_name():
	user_name = input("What is your name, user?\n")
	return user_name

def display_introductory_message(name):
	print(f"{name}, there are three stages of a woman's menstrual cycle.\n1. Menstruation (Days 1-6): The uterus sheds its lining, resulting in bleeding (menstruation).\n2. Follicular Phase (Days 6-14): The body produces follicle-stimulating hormone (FSH), which stimulates the growth of follicles in the ovaries for ovaries to mature— these follicles contain your eggs.. These follicles produce estrogen, causing the uterine lining to thicken.\n3. Luteal Phase (Days 15-28): After ovulation, the empty follicle in the ovary produces progesterone, which helps thicken the uterine lining further. If pregnancy doesn't occur, the progesterone levels drop, and the cycle starts again.\n")

def get_ovulation_date(last_period_start_date, current_period_start_date, name):
	ovulation_date = current_period_start_date + timedelta(days=14)
	print(f"Your ovulation date is {ovulation_date}\n")
	response = int(input("Do you wish to continue? \n1. Main Menu \n2. Exit\n"))
	match response:
		case 1:
			get_user_response(name, last_period_start_date, current_period_start_date)
		case 2:
			print("Thank you for using the app.\nWe hope to see you back soon.")

def get_fertile_date(last_period_start_date, current_period_start_date, name):
	fertile_date = 	current_period_start_date + timedelta(days=14)
	print(f"Your fertile window or Safe period is {fertile_date}\n")
               
	response = int(input("Do you wish to continue? \n1. Main Menu \n2. Exit\n"))
	match response:
		case 1:
			get_user_response(name, last_period_start_date, current_period_start_date)
		case 2:
			print("Thank you for using the app.\nWe hope to see you back soon.")

def get_menstrual_date(last_period_start_date, current_period_start_date, name):
	days_between_periods = abs((last_period_start_date - current_period_start_date).days)
	next_menstrual_date = current_period_start_date + timedelta(days=days_between_periods)
	print(f"Your next menstrual period date is {next_menstrual_date}\n")
	response = int(input("Do you wish to continue? \n1. Main Menu \n2. Exit\n"))
	match response:
		case 1:
			get_user_response(name, last_period_start_date, current_period_start_date)
		case 2:
			print("Thank you for using the app.\nWe hope to see you back soon.")

def get_flow_date(last_period_start_date, current_period_start_date, name):
	days_between_periods = abs((last_period_start_date - current_period_start_date).days)
	print(f"Your flow date is {days_between_periods} days\n")
	
	if days_between_periods < 21:
		print("You seem to have a short cycle also known as Polymenorrhea.\nGo and see a doctor\n")
	elif days_between_periods > 21 and days_between_periods < 34:
		print("You have a normal estimated cycle\n")
	elif days_between_periods > 35:
		print("You seem to have an abnormal cycle also known as Oligomenorrhea \nGo and see a doctor\n")
	elif days_between_periods > 50:
		print("You do not have a menstrual cycle\n Go and see a doctor as soon as possible!!\n")
	elif days_between_periods <= 0:
		println("Invalid dates inputed!!\n")

	response = int(input("Do you wish to continue? \n1. Main Menu \n2. Exit\n"))
	match response:
		case 1:
			get_user_response(name, last_period_start_date, current_period_start_date)
		case 2:
			print("Thank you for using the app.\nWe hope to see you back soon.")
	return days_between_periods


def get_user_response(name, last_period_start_date, current_period_start_date):
	user_response = int(input(f" {name}, what would you like to calculate? \n1. Calculate flow date/Menstrual cycle \n2. Calculate next menstrual period. \n3. Calculate Ovulation date \n4. Fertile window/Safe period \n"))
	match user_response:
		case 1:
			get_flow_date(last_period_start_date, current_period_start_date, name)
		case 2:
			get_menstrual_date(last_period_start_date, current_period_start_date, name)
		case 3:
			get_ovulation_date(last_period_start_date, current_period_start_date, name)
		case 4:
			get_fertile_date(last_period_start_date, current_period_start_date, name)
		case _:
			print("Invalid choice.\nPlease choose a valid option.\n")

get_welcome_message()
name = get_user_name()
display_introductory_message(name)
last_period_start_date1 = input("Enter the start date of your last period (yyyy-MM-dd): \n")
current_period_start_date1 = input("Enter the start date of your current period (yyyy-MM-dd): \n")
last_period_start_date = datetime.strptime(last_period_start_date1, "%Y-%m-%d").date()
current_period_start_date = datetime.strptime(current_period_start_date1, "%Y-%m-%d").date()
get_user_response(name, last_period_start_date, current_period_start_date)

