import datetime 

customer_name = input("What is the customer's name? ")
products = []
products_number = []
units_price = []

def display_question(products, products_number, units_price, customer_name):
	product = input("What did the user buy?\nEnter a word: ")
	products.append(product)

	product_number = int(input("How many pieces?\nEnter a number: "))
	products_number.append(product_number)

	unit_price = int(input("How much per unit?\nEnter a number: "))
	units_price.append(unit_price)

	item_confirmation = input("Add more items?\nEnter yes or no: ")

	if item_confirmation.casefold() == "yes":
		display_question(products,products_number,units_price,customer_name)
	else:
		cashiers_name = input("What is cashier's name? ")
		discount = float(input("How much discount will he get?\nEnter a number: "))
	major_display()
	extension_display(cashiers_name,customer_name)
	get_calculation(products, products_number, units_price, customer_name, discount, cashiers_name)


def get_calculation(products, products_number, units_price, customer_name, discount, cashiers_name):
		
	sub_total = 0
	print("\tITEM \tQTY \tPRICE \tTOTAL(NGN)")
	print("---------------------------------------------------------------\n")
	for index in range(len(products)):
		print(f"\t{products[index]} \t{products_number[index]} \t{units_price[index]} \t{products_number[index]*units_price[index]}\n")
		sub_total += products_number[index]*units_price[index]

	print("---------------------------------------------------------------\n")
	print(f"\tSub Total:\t{sub_total}\n")
	discount_calculated = sub_total * discount / 100
	print(f"\tDiscount:\t{discount_calculated}\n")
	vat = sub_total * 17.50 / 100
	print(f"\tVAT @ 17.50:\t{vat}\n");
	bill_total = sub_total - (discount_calculated + vat)
	print("=============================================================\n")
	print(f"\tBill Total:\t{bill_total}\n")
	print("=============================================================\n")
	print(f"THIS IS NOT A RECEIPT, KINDLY PAY {bill_total}")
	print("=============================================================\n")
		
	amount_paid = float(input(print("How much did the customer give to you? ")))
		
	if amount_paid < bill_total:
		print(f"Amount paid is less than bill total, try again!!")
		amount_paid = float(input(print("How much did the customer give to you? ")))
	get_receipt(products, products_number, units_price, customer_name, discount, cashiers_name, amount_paid)


def get_receipt(products, products_number, units_price, customer_name, discount, cashiers_name, amount_paid):
	major_display()
	extension_display(cashiers_name,customer_name)
	sub_total = 0
	print("\tITEM \tQTY \tPRICE \tTOTAL(NGN)")
	print("---------------------------------------------------------------\n")
	for index in range(len(products)):
		print(f"\t{products[index]} \t{products_number[index]} \t{units_price[index]} \t{products_number[index]*units_price[index]}\n")
		sub_total += products_number[index]*units_price[index]

	print("---------------------------------------------------------------\n")
	print(f"\tSub Total:\t{sub_total}\n")
	discount_calculated = sub_total * discount / 100
	print(f"\tDiscount:\t{discount_calculated}\n")
	vat = sub_total * 17.50 / 100
	print(f"\tVAT @ 17.50:\t{vat}\n");
	bill_total = sub_total - discount_calculated + vat
	print("=============================================================\n")
	print(f"\tBill Total:\t{bill_total}\n")
	print("=============================================================\n")
		
	balance = amount_paid - bill_total
	print(f"\tBalance:\t{balance}\n")
	print("=============================================================\n")
	print("\tTHANK YOU FOR YOUR PATRONAGE\n")
	print("=============================================================\n");


def major_display():
	print("SEMICOLON STORES\n")
	print("MAIN BRANCH\n")
	print("LOCATION: 312, HERBERT MACAULAY WAY, SABO, YABA, LAGOS STATE.\n")
	print("TEL : 03293828343\n")

def extension_display(cashiers_name,customer_name):
	today = datetime.date.today()
	print(today)
	print(f"Cashier: {cashiers_name}")
	print("Customer's Name: {customer_name}")
	print("================================================================")

display_question(products,products_number,units_price,customer_name)