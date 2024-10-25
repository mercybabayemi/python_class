weight_in_pounds = float(input("Enter your weight in pounds: "))
 
height_in_inches= float(input("Enter your height in inches:"))

calculation = (weight_in_pounds * 703) / (height_in_inches * height_in_inches)

print(f"The calculated BMI value is {calculation:.2f}")
	
if calculation < 18.5:
    print("The BMI category is underweight")
	
elif calculation >= 18.5 and calculation <= 24.9:
    print("The BMI category is normalweight")

elif calculation >= 25.0 and calculation <= 29.9:
    print("The BMI category is overweight")

elif calculation >= 30.0:
    print("The BMI category is obese")

else:
    print("The BMI category is morbidly obese") 
