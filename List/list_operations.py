# Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Append - adds an element at the end
my_list.append(60)
print("After append(60):", my_list)

# Insert - adds an element at a specific index
my_list.insert(2, 25)
print("After insert(2, 25):", my_list)

# Extend - adds elements from another list
my_list.extend([70, 80])
print("After extend([70, 80]):", my_list)

# Remove - removes the first matching value
my_list.remove(30)
print("After remove(30):", my_list)

# Pop - removes element by index (default last)
my_list.pop()
print("After pop():", my_list)

# Index - finds the index of a value
index_25 = my_list.index(25)
print("Index of 25:", index_25)

# Count - count occurrences of a value
count_20 = my_list.count(20)
print("Count of 20:", count_20)

# Reverse - reverse the list
my_list.reverse()
print("After reverse():", my_list)

# Sort - sorts the list
my_list.sort()
print("After sort():", my_list)

# Copy - creates a shallow copy of the list
copied_list = my_list.copy()
print("Copied List:", copied_list)

# Clear - removes all elements
copied_list.clear()
print("After clear() on copied list:", copied_list)

# Slicing - getting parts of a list
print("First 3 elements:", my_list[:3])
print("Last 2 elements:", my_list[-2:])

# Length, Sum, Min, Max
print("Length of list:", len(my_list))
print("Sum of list:", sum(my_list))
print("Minimum:", min(my_list))
print("Maximum:", max(my_list))

# Iterating through the list
print("Iterating:")
for item in my_list:
    print(item)
