class Stack:
    def __init__(self):
        self.st = []

    def is_empty(self):
        return self.st == []
    def push(self, ele):
        self.st.append(ele)
    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.st.pop()
    def peep(self):
        n = len(self.st)
        return self.st[n-1]
    def search(self, element):
        if self.is_empty():
            return -1
        else:
            try:
                n = self.st.index(element)
                return n
            except ValueError:
                return -2
    def display(self):
        return self.st
from Stack import Stack
s = Stack()
choice = 0
while choice < 5:
    print("STACK OPERATIONS")
    print("1 for PUSH")
    print("2 for POP")
    print("3 for PEEP")
    print("4 for Search")
    print("5 for Exit")
    
    choice = int(input("Enter your choice(1-5): "))
    if choice == 1:
        element = input("Enter Push element: ")
        s.push(element)
    elif choice == 2:
        ele = s.pop()
        if ele == -1:
            print("Stack is empty")
        else:
            print(f"popped element: {ele}")
    elif choice == 3:
        elem = s.peep()
        print(f"Topmost element = {elem}")
    elif choice == 4:
        el = input("Enter the search element: ")
        pos = s.search(el)
        if pos == -1:
            print("The Stack is empty")
        elif pos == -2:
            print("Element not found in the Stack")
        else:
            print(f"Element found at index {pos}.")
    else:
        break

    print(f"Stack: {s.display()}")