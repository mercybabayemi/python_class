first_citizen_earning = int(input("Enter first citizen's earning: "))
	
first_citizen_name = input("Enter first citizen's name: ")

second_citizen_earning = int(input("Enter second citizen's earning: "))
	
second_citizen_name = input("Enter second citizen's name: ")

third_citizen_earning =  int(input("Enter third citizen's earning: "))

third_citizen_name = input("Enter third citizen's name: ")

tax_rate = 0
first_total_tax= 0
second_total_tax = 0
third_total_tax = 0

if first_citizen_earning <= 30000:
	tax_rate = 15 / 100
	first_total_tax = first_citizen_earning * tax_rate
	print(first_citizen_name, "'s earning of", first_citizen_earning, "total tax is", first_total_tax )

elif first_citizen_earning > 30000:
	tax_rate = 20 / 100
	first_total_tax = first_citizenc_earning * tax_rate
	print(first_citizen_name, "'s earning of", first_citizen_earning, "total tax is", first_total_tax )



if second_citizen_earning <= 30000:
	taxRate = 15 / 100
	second_total_tax = second_citizen_earning * tax_rate
	print(second_citizen_name, "'s earning of ", second_citizen_earning, " total tax is " , second_total_tax )
	
elif second_citizen_earning > 30000:
	tax_rate = 20 / 100
	second_total_tax = secondCitizenEarning * taxRate
	print(second_citizen_name, "'s earning of ", second_citizen_earning, " total tax is " , second_total_tax )


if third_citizen_earning <= 30000:
	tax_rate = 15 / 100
	third_total_tax = third_citizen_earning * tax_rate
	print(third_citizen_name, "'s earning of ", third_citizen_earning,  " total tax is ", third_total_tax )

elif third_citizen_earning > 30000:
	tax_rate = 20 / 100
	third_total_tax = third_citizen_earning * tax_rate
	print(third_citizen_name, "'s earning of ", third_citizen_earning,  " total tax is ", third_total_tax )
