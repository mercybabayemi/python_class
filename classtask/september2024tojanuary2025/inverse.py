number = int(input("Enter between 100 - 999: "))

first_number = number % 10

second_trial = number // 10

second_number = second_trial % 10

third_number = number // 100

print(first_number, second_number, third_number)

even_number = 0
odd_number = 0

if(first_number % 2 == 0):even_number += 1
else:odd_number += 1

if(second_number % 2 == 0):even_number += 1
else:odd_number += 1


if(third_number % 2 == 0):even_number += 1
else:odd_number += 1

print("Odd number is ", odd_number)
print("Even number is ", even_number)


