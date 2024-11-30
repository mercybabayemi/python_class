principal = float(input("Enter amount invested: "))

rate = float(input("Enter rate: "))

PERCENTAGE_CONVERTER = 1 / 100

annual_rate = rate * PERCENTAGE_CONVERTER

amount_deposit_in_ten_years = principal * ( 1 + annual_rate) ** 10

amount_deposit_in_twenty_years = principal * ( 1 + annual_rate) ** 20

amount_deposit_in_thirty_years = principal * ( 1 + annual_rate) ** 30


print(f"The amount on deposit at the end of ten years is {amount_deposit_in_ten_years:.2f}")

print(f"The amount on deposit at the end of twenty years is {amount_deposit_in_twenty_years:.2f}")

print(f"The amount on deposit at the end of thirty years is {amount_deposit_in_thirty_years:.2f}")



