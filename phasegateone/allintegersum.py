"""
pseudocode of integer palindrome
- prompt user for a number between 0 and 1000
- declare an empty list 
- declare total to 0
- separate figure from each other 
- append number to the list
- loop through and sum each figures
"""

number = int(input("Enter a number between 0 to 1000 :"))
if number < 0 or number > 1000:
	print("Invalid input!!!")
	number = int(input("Enter a number between 0 to 1000 :"))

numbers = []
total = 0
first_number = number % 10
numbers.append(first_number)

second_trial = number // 10
second_number = second_trial % 10
numbers.append(second_number)

third_number = number // 100
numbers.append(third_number)

for each_number in range(len(numbers)):
	total += numbers[each_number]
print(f"The total is {total}.")