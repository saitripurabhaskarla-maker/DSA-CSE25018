class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = None

def push():
    global top

    x = int(input("Enter element: "))

    new_node = Node(x)
    new_node.next = top
    top = new_node

    print("Element pushed")


def pop():
    global top

    if top is None:
        print("Stack Underflow")
    else:
        print("Deleted:", top.data)
        top = top.next


def peek():
    if top is None:
        print("Stack is empty")
    else:
        print("Top element:", top.data)


def display():
    if top is None:
        print("Stack is empty")
    else:
        temp = top

        print("Stack:", end=" ")

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()


while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
        
