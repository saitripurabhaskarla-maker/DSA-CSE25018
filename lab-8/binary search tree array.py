
SIZE = 100
tree = [None] * SIZE

def insert(value):
    i = 0

    while i < SIZE:
        if tree[i] is None:
            tree[i] = value
            print("Inserted successfully")
            return

        if value < tree[i]:
            i = 2 * i + 1
        elif value > tree[i]:
            i = 2 * i + 2
        else:
            print("Duplicate value")
            return

    print("Tree is full")

def search(value):
    i = 0

    while i < SIZE and tree[i] is not None:
        if tree[i] == value:
            print("Value found")
            return
        elif value < tree[i]:
            i = 2 * i + 1
        else:
            i = 2 * i + 2

    print("Value not found")

def inorder(i):
    if i >= SIZE or tree[i] is None:
        return
    inorder(2 * i + 1)
    print(tree[i], end=" ")
    inorder(2 * i + 2)

def preorder(i):
    if i >= SIZE or tree[i] is None:
        return
    print(tree[i], end=" ")
    preorder(2 * i + 1)
    preorder(2 * i + 2)

def postorder(i):
    if i >= SIZE or tree[i] is None:
        return
    postorder(2 * i + 1)
    postorder(2 * i + 2)
    print(tree[i], end=" ")

while True:
    print("\n\n1.Insert 2.Search")
    print("3.Inorder  4.Preorder")
    print("5.Postorder  6.Display  7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        insert(int(input("Enter value: ")))
    elif choice == 2:
        search(int(input("Enter value: ")))
    elif choice == 3:
        inorder(0)
        print()
    elif choice == 4:
        preorder(0)
        print()
    elif choice == 5:
        postorder(0)
        print()
    elif choice == 6:
        print([x for x in tree if x is not None])
    elif choice == 7:
        break
    else:
        print("Invalid choice")
