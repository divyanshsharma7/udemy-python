my_dict = {
    "apple": 10,
    "banana": 5,
    "cherry": 8,
    "date": 12
}

print("Original Dictionary:", my_dict)

# Convert dictionary keys and values to lists
keys_list = list(my_dict.keys())  # List of keys
values_list = list(my_dict.values())  # List of values

# Append a new item (similar to list.append)
my_dict["elderberry"] = 7  # Equivalent to adding an element

# Remove an item (similar to list.remove)
del my_dict["banana"]  # Equivalent to list.remove()

# Update an item (similar to list indexing)
my_dict["cherry"] = 15  # Updating a value

# Sort keys and values separately (like list.sort)
sorted_keys = sorted(my_dict.keys())
sorted_values = sorted(my_dict.values())

# Reverse keys and values separately (like list.reverse)
reversed_keys = list(my_dict.keys())[::-1]
reversed_values = list(my_dict.values())[::-1]

# Insert an item (similar to list.insert)
# Dictionaries don't support direct insertion, but we can create an ordered dictionary
from collections import OrderedDict
my_dict = OrderedDict(my_dict)
my_dict.update({"fig": 6})  # This adds at the end
my_dict.move_to_end("fig", last=False)  # Moves "fig" to the beginning

# Pop an item (similar to list.pop)
popped_item = my_dict.pop("date")

# Extend dictionary (similar to list.extend)
my_dict.update({"grape": 9, "honeydew": 4})

# Display results
print("Updated Dictionary:", my_dict)
print("Sorted Keys:", sorted_keys)
print("Sorted Values:", sorted_values)
print("Reversed Keys:", reversed_keys)
print("Reversed Values:", reversed_values)
print("Popped Item:", popped_item)