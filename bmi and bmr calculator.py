import sys

print("Please enter either 'Metric' or 'Imperial' to set the calculator's properties.")

Age = int(input("Please Enter your age"))
Gender = str(input("Please enter whether you are male or female"))
Weight = float(input("Please enter your weight in Kilograms(Kg): "))
Height = float(input("Please enter your Height centimeters(cm): "))
Height /= 100
BMI = Weight / (Height ** 2)
print("Your Body Mass Index (BMI) is: " + "{:.2f}".format(BMI))



