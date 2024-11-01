sum = 0
counter = 1
stop = -1

while counter <= 2:
	number = int(input("Enter number or -1 to terminate: "))

	sum = sum + number
	counter = counter + 1
		
	if number != stop:
		continue
		
	else:
		break

if sum >= 0:
	print("The sum is ", sum)
else:
	print( "Loop terminated")