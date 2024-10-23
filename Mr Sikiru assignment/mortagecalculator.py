amount = int(input("Enter the principal amount: "))
annual_rate = int(input("Enter the annual interest rate: "))
duration_in_years = int(input("Enter the duration in years: "))
monthly_rate = annual_rate / 100 / 12
number_of_months = duration_in_years * 12
monthly_payment = amount * (( monthly_rate * ( 1 + monthly_rate ) ** number_of_months ) / (( 1 + monthly_rate ) ** number_of_months - 1 ))
print(f"monthly_payment: {monthly_payment:.2f}")

