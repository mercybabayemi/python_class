days = int(input("Enter number of days lateness before book was returned: "))
for index in range(1):
	if days <= 5:
		print("Fine is 50 paise")
	elif days == 6 or days <= 10:
		print("Fine is 1 rupee")
	elif days > 10 and days < 30:
		print("Fine is 5 rupees")
	elif days >= 30:
		print("Membership cancelled")
