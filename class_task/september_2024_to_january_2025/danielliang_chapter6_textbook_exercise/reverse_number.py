def reverse_number(number):
    extracted_number = number
    number_string = ""
    number_str = str(number)
    number_length = len(number_str)

    while number_length != 0:
        removedNumber = extracted_number % 10
        number_string = number_string + str(removedNumber)
        extracted_number = extracted_number//10
        number_length -= 1

    if number_string == str(number):
        print("The number is a palindrome")
    if number_string != str(number):
        print("The number is not a palindrome")

    return number_string

print(reverse_number(121))