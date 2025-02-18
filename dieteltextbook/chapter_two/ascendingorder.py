first_number = float (input("Enter a float number: "))

second_number = float (input("Enter second float number: "))

third_number = float (input("Enter third float number: "))


if first_number < second_number < third_number:
    print(first_number, second_number, third_number)
elif first_number < third_number < second_number:
    print(first_number, third_number, second_number)
elif second_number > third_number and first_number:
    print(second_number, third_number, first_number)
elif second_number < first_number and third_number:
    print(second_number, first_number, third_number)
elif third_number < first_number and second_number:
    print(third_number, first_number, second_number)
elif third_number < second_number and first_number:
    print(third_number, second_number, first_number)
