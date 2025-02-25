
#  Check if a Number is Even or Odd

# User Input Number

#Prompt the user to enter the number and converts the input to an integer
number = int(input("Enter a number : "))

# Checking if the number is less than ZERO
while number < 0:
    print("Please enter a number greater than ZERO")
    number = int(input("Enter a number : "))

if (number % 2) == 0: #checking if the number is divisible by 2
    print(f"{number} is an Even Number")
else:
    print(f"{number} is an Odd Number")
