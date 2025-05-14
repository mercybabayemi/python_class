from src.exceptions.invalid_symbol_exception import InvalidSymbolException

class Calculate:
    symbols = ['*', '/', '%', '+', '-']
    def calculate_with_different_arithmetic_symbol(*data):
        symbols_used_count = count_all_symbols(*data)
        for _ in range(1,symbols_used_count):
            for each in data:
                multiplication_index = check_multiplication_index(data)



symbols = ['*', '/', '%', '+', '-']
def check_multiplication_index(*data):
    count = 0
    return_variable = []
    for each in data:
        count += 1
        if each not in symbols:
            raise InvalidSymbolException("Symbol unavailable for usage.")
        elif int(each):
            pass
        elif not int(each):
            if each == symbols[0]:
                return_variable.append(count)
    return return_variable

def check_division_index(*data):
    count = 0
    return_variable = []
    for each in data:
        count += 1
        if each not in symbols:
            raise InvalidSymbolException("Symbol unavailable for usage.")
        elif int(each):
            pass
        elif not int(each):
            if each == symbols[1]:
                return_variable.append(count)
    return return_variable

def check_modulo_index(*data):
    count = 0
    return_variable = []
    for each in data:
        count += 1
        if each not in symbols:
            raise InvalidSymbolException("Symbol unavailable for usage.")
        elif int(each):
            pass
        elif not int(each):
            if each == symbols[1]:
                return_variable.append(count)
    return return_variable

def check_addition_index(*data):
    count = 0
    return_variable = []
    for each in data:
        count += 1
        if each not in symbols:
            raise InvalidSymbolException("Symbol unavailable for usage.")
        elif int(each):
            pass
        elif not int(each):
            if each == symbols[1]:
                return_variable.append(count)
    return return_variable

def check_subtraction_index(*data):
    count = 0
    return_variable = []
    for each in data:
        count += 1
        if each not in symbols:
            raise InvalidSymbolException("Symbol unavailable for usage.")
        elif int(each):
            pass
        elif not int(each):
            if each == symbols[1]:
                return_variable.append(count)
    return return_variable

def count_all_symbols(*data):
    count = 0
    for each in data:
        if each not in symbols:
            raise InvalidSymbolException("Symbol unavailable for usage.")
        elif int(each):
            pass
        elif not int(each):
            count += 1
    return count