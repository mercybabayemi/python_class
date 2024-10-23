number = 0
largestNumber = 0
smallestNumber = 0
	
while true:
    userInput = int(input("Enter number: "))
		

    if userInput > largestNumber:
        largestNumber = userInput
    if userInput < smallestNumber:
        smallestNumber = userInput

    answer = int(input("DO you wish to continue, press 1 for(Yes) or 2 for(no) to exit"))

    if answer == 1:
        continue
    elif answer == 2:
        break

print(f"The largest number is {largestNumber}")
print(f"The smallest number is {smallestNumber}")

