# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Task 1
name = input("Enter your name: ")
surname=input("Enter your surname: ")
age=input("Enter your age: ")
print("Your name is: " + name + " .Your surname is: "+ surname+ " .Your age is : "+age )
# Task 2
farenheit = float(input("Enter temperature in Farenheit: "))

# Convert Celsius to Fahrenheit

celsius= (farenheit-32)/(9/5)
# Print the converted temperature
print("Temperature in Celsius:", celsius)
#Task 3
# Define variable
score = float(input("Enter your score: "))

# Determine the grade
if score >= 90:
    grade = "5"
elif score >= 80:
    grade = "4"
elif score >= 70:
    grade = "3"
elif score >= 60:
    grade = "2"
else:
    grade = "1"

class_grade = (grade*0,2)
test_grade = (grade*0,3)
project_grade = (grade*0,5)
# Print the grade
print("Your score is:" , str(grade))
print( "Your class grade is : ", str(class_grade))
print("Your test grade is : ", str(test_grade))
print( "Your project grade is : ", str(project_grade))
# Task 4
# Define variable

number1 = int(input("Enter a number 1: "))

number2 = int(input("Enter a number 2: "))

# Check if the number is even or odd

if number2 == 0:

    result = "You can`t divide by 0 "

else:

    if number1%number2==0:

      result = "Number 1 is separated by second"

    else:

      result = "Number 1 can not be  separated by second"

# Print the result

print(result)

#Task 5
# Define variables
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    # Check the type of triangle
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    print("The triangle is:", triangle_type)
else:
    print("Triangle cannot be created with such lengths.")
    #Task 6
