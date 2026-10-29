
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

root = None

def insert(node, value):
    if node is None:
        return Node(value)

    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    else:
        print("Duplicate value not allowed")

    return node

def search(node, value):
    if node is None:
        print("Value not found")
    elif node.data == value:
        print("Value found")
    elif value < node.data:
        search(node.left, value)
    else:
        search(node.right, value)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

while True:
    print("\n--- BST LINKED LIST MENU ---")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder")
    print("4. Preorder")
    print("5. Postorder")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        root = insert(root, value)
        print("Insertion operation completed")

    elif choice == 2:
        value = int(input("Enter value to search: "))
        search(root, value)

    elif choice == 3:
        print("Inorder:", end=" ")
        inorder(root)
        print()

    elif choice == 4:
        print("Preorder:", end=" ")
        preorder(root)
        print()

    elif choice == 5:
        print("Postorder:", end=" ")
        postorder(root)
        print()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
