#PalindromeInteger

number = int(input("Enter a number between 0 to 1000 :"))


first_number = number % 10

second_trial = number // 10
second_number = second_trial % 10

third_number = number // 100 

print(first_number, second_number, third_number) 



if first_number != third_number:
    print(f"Integer is not a palindrome integer")
	
elif first_number == third_number:
    print(f"Integer is a palindrome integer")
