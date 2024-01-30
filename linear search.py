def linear_search(lst, target):
    for i, element in enumerate(lst):
        if element == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Get user input for the list elements
num_elements = int(input("Enter the number of elements: "))
user_list = [input(f"Enter element {i + 1}: ") for i in range(num_elements)]

# Get user input for the target value to search
target_value = input("Enter the value to search for: ")

# Perform linear search
result = linear_search(user_list, target_value)

# Display the result
if result != -1:
    print(f"{target_value} found at index {result}")
else:
    print(f"{target_value} not found in the list") 