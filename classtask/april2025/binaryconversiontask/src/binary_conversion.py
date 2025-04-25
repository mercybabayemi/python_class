from exceptions import value_not_binary_exception


def convert_binary_to_base_ten(*binary: str):
    calculation: int = 0
    for value in binary:
        for item in value:
            length: int = len(value)

            if int(item) == 1 or int(item) == 0:
                for each in item:
                    calculated = int(each) * (2 ** (length - 1))
                    calculation += calculated
                    length -= 1
                    if length == 0:
                        return
            elif int(item) > 1:
                raise value_not_binary_exception

    return calculation