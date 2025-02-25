# Sum of integers from 1 to 50 using a Loop

# defining variable

sum = 0 #initialising the variable sum to 0, This variable will hold the sum of integers

for number in range(1,51): #Iterates over a range from 1 to 50 inclusive
    sum = sum + number #adds the current number to the variable

print(f"The sum of numbers from 1 to 50 is {sum}")