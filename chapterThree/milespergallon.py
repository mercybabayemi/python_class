gallons = 0
miles = 0
total_miles_sum = 0
total_gallons_sum = 0
average = 0
count = 0
while gallons != -1:
	miles = int(input('Enter the miles driven: '))
	gallons = int(input('Enter the gallons used(-1 to end): '))
	miles_per_gallon = miles / gallons
	if gallons != -1:
		print('The miles per gallon for this tank is ', miles_per_gallon)
		total_miles_sum += miles
		total_gallons_sum += gallons
		average = total_miles_sum / total_gallons_sum
	count += 1

print('The overall average miles/gallon was ', average)
	