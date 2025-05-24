# Initial list
courses = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']
print("Original first item:", courses[0])

# Modify an element
courses[0] = 'eac150'
print("Updated first item:", courses[0])
print("Updated list:", courses)

# Add an item at the end
courses.append('ops235')
print("After append:", courses)

# Insert at the beginning
courses.insert(0, 'hwd101')
print("After insert at index 0:", courses)

# Remove a specific item
courses.remove('ops335')
print("After removing 'ops335':", courses)

# Copy and sort
sorted_courses = courses.copy()
sorted_courses.sort()
print("Original list after copy:", courses)
print("Sorted copy:", sorted_courses)

# Use built-in functions on numeric list
list_of_numbers = [1, 5, 2, 6, 8, 5, 10, 2]
length_of_list = len(list_of_numbers)
smallest_in_list = min(list_of_numbers)
largest_in_list = max(list_of_numbers)

print("List length is " + str(length_of_list) + 
      ", smallest element in the list is " + str(smallest_in_list) +
      ", largest element in the list is " + str(largest_in_list))
