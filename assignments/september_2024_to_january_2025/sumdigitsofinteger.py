#SumDigitsOfInteger

number = int(input("Enter a number between 0 to 1000: "))

first_number = number % 10 

second_trial = number // 10

second_number = second_trial % 10

third_number = number // 100

sum = first_number + second_number + third_number

print(f"Sum of all the digits in the integer is {sum}") 
