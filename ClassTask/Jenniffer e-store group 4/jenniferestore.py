def main_menu():
	print("""
		Welcome to Jennifer's E-Store! 
		1. View Products 
		2. Add to Cart 
		3. Remove from Cart 
		4. View Cart 
		5. Checkout 
		6. Exit 
		""")
	print(f"You have {len(cart[0])} products in cart.")
	user_input = int(input("Enter a number value: "))
	match user_input:
		case 1: get_view_products()
		case 2: add_to_cart()
		case 3: remove_from_cart()
		case 4: view_cart()
		case 5: checkout()
		case 6: exit()
		case _: return "invalid input"

def get_view_products():
	for index in range(len(products_catalogue[0])):
		print(f"{index + 1}.{products_catalogue[0][index]}   {products_catalogue[1][index]}")
	print("""
		Do you want to go back?
		1. Back
		2. Exit
		""")
	user_input = int(input("Enter a number value: "))
	match user_input:
		case 1: main_menu()
		case 2: exit()
		case _: return "invalid input"

def add_to_cart():
	for index in range(len(products_catalogue[0])):
		print(f"{index + 1}.{products_catalogue[0][index]}   {products_catalogue[1][index]}")
	user_input = int(input("Enter a number value: "))
	cart[0].append(products_catalogue[0][user_input - 1])
	cart[1].append(products_catalogue[1][user_input - 1])
	print(f"{products_catalogue[0][user_input - 1]} has been added to your cart!!!")
	main_menu()

def remove_from_cart():
	for index in range(len(cart[0])):
		print(f"{index + 1}.{cart[0][index]}")
	user_input = int(input("Enter a number value: "))

	if len(cart) > 1:
		removed = cart[0].pop([0][user_input - 1])
		cart[1].pop([0][user_input - 1])
		print(f"{removed} have been removed from your cart!!!")
		main_menu()
	else:
		print("No index")
		main_menu()
def view_cart():
	for index in range(len(cart)):
		print(f"{index + 1}.{cart[0][index]}  {cart[1][index]}")
	user_input = int(input("Do you want to checkout?\nPress 1 for yes.\nPress 2 to go back to main menu: "))
	if response == 1:
		check_out()
	elif response == 2:
		main_menu()
	else:
		print("Invalid input!! Returning to main menu....")
		main_menu()

def checkout(): 
	total = 0
	for index in range(len(cart[0])):
		total += cart[1][index]
		print(f"{index + 1}. {cart[0][index]}  {cart[1][index]}")
	print(f"The total price is {total}")
	cart[0].clear()
	cart[1].clear()
	user_input = int(input("Would you like to go back to main menu or exit?\n1. Main menu\n2. exit  "))
	if user_input == 1:
		main_menu()
	else:
		exit()

def exit():
	print("Thank you for shopping with us...")


products_catalogue = [["Laptop","Phone","Headphone"],[1000,500,100]]
cart = [[],[]]
main_menu()


