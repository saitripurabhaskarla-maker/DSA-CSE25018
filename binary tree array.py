
SIZE = 100
tree = []
 
def insert(value):
    if len(tree) >= SIZE:
        print("Tree is full!")
        return

    tree.append(value)
    print("Node inserted successfully.")

def inorder(i):
    if i >= len(tree):
        return

    inorder(2 * i + 1)
    print(tree[i], end=" ")
    inorder(2 * i + 2)

def preorder(i):
    if i >= len(tree):
        return

    print(tree[i], end=" ")
    preorder(2 * i + 1)
    preorder(2 * i + 2)

def postorder(i):
    if i >= len(tree):
        return

    postorder(2 * i + 1)
    postorder(2 * i + 2)
    print(tree[i], end=" ")

while True:
    print("\n\n--- BINARY TREE MENU ---")
    print("1. Insert")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Display Array")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        insert(value)

    elif choice == 2:
        print("Inorder:", end=" ")
        inorder(0)
        print()

    elif choice == 3:
        print("Preorder:", end=" ")
        preorder(0)
        print()

    elif choice == 4:
        print("Postorder:", end=" ")
        postorder(0)
        print()

    elif choice == 5:
        print("Tree array:", tree)

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
