# Write a python program to swap elements of a list consecutive pairwise.
# let's assume range=1-2 so lst[0] will store 2 and lst[1] will store 1.
# it's mean store even numbers to lst[even] and odd to lst[odd] within a range.
def swap_consecutive_pairs(lst):
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]

# Get user input for the size of the list
list_size = int(input("Enter the size of the list: "))

# Create a list and fill it with values based on consecutive pairwise swapping
my_list = [i+1 for i in range(list_size)]
swap_consecutive_pairs(my_list)

print("List with consecutive pairwise swapping:",my_list)
