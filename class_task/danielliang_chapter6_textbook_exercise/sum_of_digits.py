def sum_of_digits(n):
    extracted_number = n
    sum = 0
    number_string = str(n)
    number_string_length = len(number_string)

    while number_string_length != 0:
        removed_digits = extracted_number % 10
        sum += removed_digits
        extracted_number //= 10
        number_string_length -= 1

    return sum


print(sum_of_digits(234))
