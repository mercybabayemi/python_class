def get_even_from_string(message):
    num = [int(item) for item in message if item.isdigit()]
    result = [item for item in num if item % 2 == 0]
    return result
