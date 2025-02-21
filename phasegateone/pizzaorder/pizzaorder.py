import math
def number_of_people_determinant(customer_name):
	number_of_people = int(input(f"{customer_name}, how many people are coming to your party?\n"))
	while number_of_people <= 0:
		print("Not a valid input, please enter a valid number.\n")	
		number_of_people = int(input(f"{customer_name}, how many people are coming to your party?\n"))
	return number_of_people

def get_pizza_type_choice(pizza_type):
	pizza_type_choosing = int(input("What size of pizza type do you want?\nEnter the number value\n1. Sapa size = 4 slices\n2. Small money = 6 slices\n3. Big boys = 8 slices\n4. Odogwu = 12 slices\n"))
	return pizza_type_choosing

def get_pizza_type(pizza_type, pizza_type_choosing):
		pizza_choice = pizza_type[pizza_type_choosing - 1]
		return f"Pizza type = {pizza_choice}"

def get_number_of_pizza_box_to_buy(slice_to_consider, number_of_slices, pizza_type_choosing):
	number_of_box = math.ceil(slice_to_consider / number_of_slices[pizza_type_choosing - 1])
	print(f"Number of pizza boxes to buy is {number_of_box}")
	return number_of_box

def get_left_over(slice_to_consider, number_of_slices, pizza_type_choosing):
	left_over = slice_to_consider % number_of_slices[pizza_type_choosing - 1];
	return f"Number of slices leftover is {left_over}"

def get_price(price_per_box, pizza_type_choosing, numbered_box):
	price_to_pay = price_per_box[pizza_type_choosing - 1] * numbered_box
	return f"Please, pay {price_to_pay} Naira for your pizza."

print("Welcome to Iya Moses Pizza joint,Ajegunle.\n")

customer_name = input("What is your name, customer? \n")
	
pizza_type = ["Sapa size","Small money","Big boys","Odogwu"]
number_of_slices = [4,6,8,12]
price_per_box = [2500, 2900, 4000, 5200]

slice_to_consider = number_of_people_determinant(customer_name)
pizza_type_choosing = get_pizza_type_choice(pizza_type)
print(get_pizza_type(pizza_type, pizza_type_choosing))
numbered_box = get_number_of_pizza_box_to_buy(slice_to_consider, number_of_slices, pizza_type_choosing)
print(get_left_over(slice_to_consider, number_of_slices, pizza_type_choosing))
print(get_price(price_per_box, pizza_type_choosing, numbered_box))
