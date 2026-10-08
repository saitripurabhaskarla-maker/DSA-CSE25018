stack = []
MAX = 5

def push():
    if len(stack) == MAX:
        print("Stack Overflow")
    else:
        x = int(input("Enter element: "))
        stack.append(x)
        print("Element pushed")

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Deleted:", stack.pop())

def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack:", stack)

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
