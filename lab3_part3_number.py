def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

# Store the return value in a variable
number = return_number_value()

# Print the number and do math with it
print(number)
print(number + 5)
print(return_number_value() + 10)

# Combining number with string - WRONG way (will cause error)
 print('my number is ' + number)  # <-- This line will cause an error

# Correct ways to combine number with string
print('my number is', number)
print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))
