import sys


def getPentagonalNumber(n):
    count = 0
    for i in range(1, 101):
        formula_result =str ( (i * (3 * i - 1) // 2))
        count += 1
        sys.stdout.write(formula_result + " ")

        if count % 10 == 0:
            sys.stdout.write('\n')


    return "";

getPentagonalNumber(100)