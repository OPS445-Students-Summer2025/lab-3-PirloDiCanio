# Example 1: Simple loop
list_of_numbers = [1, 5, 2, 6, 8, 5, 10, 2]
for item in list_of_numbers:
    print(item)

# Example 2: Square each number
def square(num):
    return num * num

print("\nSquares:")
for value in list_of_numbers:
    print(square(value))

# Example 3: Return a new list with squares
def square_list(number_list):
    new_list = []
    for number in number_list:
        new_list.append(number * number)
    return new_list

new_list = square_list(list_of_numbers)
print("\nOriginal List:", list_of_numbers)
print("Squared List:", new_list)

# Example 4: Remove values by reference
def delete_numbers(numbers):
    numbers.remove(5)
    numbers.remove(6)
    numbers.remove(8)
    numbers.remove(5)

delete_numbers(list_of_numbers)
print("\nModified List:", list_of_numbers)
