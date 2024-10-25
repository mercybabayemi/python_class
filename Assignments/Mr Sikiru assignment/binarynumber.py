number = int(input("Enter an integer number: "))

firstNumber = number % 2;
secondTrial = number // 2;
secondNumber = secondTrial % 2;
thirdTrial = number // 2;
thirdNumber = thirdTrial // 2;

print(firstNumber, secondNumber, thirdNumber);
