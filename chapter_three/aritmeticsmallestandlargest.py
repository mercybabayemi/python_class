sum = 0
total = 4
count = 0
product = 1
largest = 0
smallest = 0
while count < 4:
	number = int(input('Enter number: '))
	sum = sum + number
	product = product * number
	average = sum / total
	if smallest > number:
		smallest = number
	if largest < number:
		largest = number
	range = largest - smallest
	count = count + 1

print('Final sum is ', sum)
print('Average is ', average)
print('Product is ', product)
print('Range is: ', range)
print('Smallest number is ', smallest)
print('Largest number is ', largest)