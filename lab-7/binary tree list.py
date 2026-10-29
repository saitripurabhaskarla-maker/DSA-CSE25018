
tree = []

def insert(value):
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
    print("\n\n1. Insert")
    print("2. Inorder")
    print("3. Preorder")
    print("4. Postorder")
    print("5. Display List")
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
        print("Tree list:", tree)

    elif choice == 6:
        break

    else:
        print("Invalid choice!")
