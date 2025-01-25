principal = float(input("Enter amount invested: "))

rate = float(input("Enter rate: "))

for year in range(1,31):
	percentage_converter = 1 / 100

	annual_rate = rate * percentage_converter

	amount_deposit_in_years = principal * ( 1 + annual_rate) ** year
		
	for number in range(1):

		print(f"The amount on deposit at the end of year {year} is {amount_deposit_in_years:.2f}")

print()
