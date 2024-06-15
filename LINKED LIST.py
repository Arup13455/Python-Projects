# create a empty linked list
ll = []

ll.append("America")
ll.append("Japan")
ll.append("India")
# display the existing list
print(f"The existing list: {ll}")

choice = 0
while choice < 5:
    print("LINKED LIST OPERATIONS") 
    print("1 for add element")
    print("2 for remove element")
    print("3 for replace element")
    print("4 for search any element")
    print("5 for exit")

    choice = int(input("Enter your choice(1-5): "))
    if choice == 1:
        new_ele = input("Enter the element you want to add: ")
        position = int(input("At which position: "))
        ll.insert(position, new_ele)
    elif choice == 2:
        try:
            element = input("Enter the element you want to remove: ")
            ll.remove(element)
        except ValueError:
            print("Element not found")
    elif choice == 3:
        ele = input("Enter new element: ")
        pos = int(input("At Which position? do you want to replace: "))
        ll.pop(pos)
        ll.insert(pos, ele)
    elif choice == 4:
        elem = input("Enter the element you want to search: ")
        try:
            pos = ll.index(elem)
            print(f"Element found at index{pos}.")
        except ValueError:
            print("Element not found")
    else:
        break

    print(f"List = {ll}")