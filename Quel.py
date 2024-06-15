class Queue:
    def __init__(self):
        self.qu = []
    def is_empty(self):
        return self.qu == []
    def add(self, ele):
        self.qu.append(ele)
    def delete(self):
        if self.is_empty():
            return -1
        else:
            return self.qu.pop(0)
    def search(self, elem):
        if self.is_empty():
            return -1
        else:
            try:
                n = self.qu.index(elem)
                return n
            except ValueError:
                return -2
    def display(self):
        return self.qu
    
from Quel import Queue

q = Queue()

choice = 0
while choice < 4:
    print("QUEUE OPERATIONS:")
    print("1 for Add.")
    print("2 for Delete.")
    print("3 for Search.")
    print("4 for exit.")
    choice = int(input("Enter your choice(1-4): "))

    if choice == 1:
        element = input("Enter Added element: ")
        q.add(element)
    elif choice == 2:
        element = q.delete()
        if element == -1:
            print("The Queue is empty.")
        else:
            print(f"Deleted element: {element}")
    elif choice == 3:
        elem = input("Enter the Search element: ")
        pos = q.search(elem)
        if pos == -1:
            print("The Queue is empty.")
        elif pos == -2:
            print("Element not found in the queue.")
        else:
            print(f"Element found at index{pos}.")
    else:
        break
    
    print(f"QUEUE = {q.display()}")