entree= int(input("Enter a number: "))
entree1= int(input("Enter the second number: "))
entree2= int(input("Enter the third number: "))

sum = entree + entree1 + entree2
print(f"The sum is {sum}")

product = entree * entree1 * entree2
print(f"The product is {product}")

average = sum / 3
print(f"The average is {average}")

print(f"The largest number is {max(entree,entree1,entree2)}")
print(f"The smallest number is {min(entree,entree1,entree2)}")