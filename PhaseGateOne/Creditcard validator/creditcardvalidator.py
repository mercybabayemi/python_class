def get_user_details():
	card = ""
	card = input("Enter a valid card details: ")
	if len(card) < 13 or len(card) > 16:
		card = input("Invalid card input!!\nEnter a valid card details: ")
		
	return card

def get_card_continuity():
	response = int(input("Do you want to reenter a valid card or exit?\n1. Go to enter a valid card\n2. exit\n"))
	match response:
		case 1:
			card = get_user_details()
			get_card_type(card)
		case 2:
			print("Bye!!!")

def get_card_type(card):
	if card[0] == '4':
		print("Card is a Visacard.")
	elif card[0] == '5':
		print("Card is a MasterCard.")
	elif card[0] == '3' and card[1] == '7':
		print("Card is an American Express Card.")
	elif card[0] == '6':
		print("Card is a Discovery Card.")
	else:
		print("Card has no valid type!!\n")
		get_card_continuity()

def get_credit_card_calculation(card):
	even_position_sum = 0
	odd_position_sum = 0
	for i, item in enumerate(card[::-1]):
		digit = int(item)
		if (i + 1) % 2 == 0:
			digit *= 2
			if digit > 9:
				digit -= 9
			even_position_sum += digit
		else:
			odd_position_sum += digit
	print(f"The total sum of odd numbers is {odd_position_sum}\n")

	print(f"The total sum of even numbers is {even_position_sum}\n")


	total = odd_position_sum + even_position_sum

	print(f"The total sum of all numbers is {total}\n")
		
	return total

def get_card_validity(total):
	if total % 10 == 0:
		print("Card number is valid.")
	else:
		print("Card is not valid.")


card = get_user_details()
get_card_type(card)
total = get_credit_card_calculation(card)
get_card_validity(total)
