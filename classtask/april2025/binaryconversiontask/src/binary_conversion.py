from exceptions import value_not_binary_exception


def convert_binary_to_base_ten(*binary: str):
    calculation: int = 0
    for value in binary:
        length: int = len(value)
        for item in value:

            if int(item) == 1 or int(item) == 0:
                    calculated = int(item) * (2 ** (length - 1))
                    calculation += calculated
                    length -= 1

            elif int(item) > 1:
                raise value_not_binary_exception

    return calculation