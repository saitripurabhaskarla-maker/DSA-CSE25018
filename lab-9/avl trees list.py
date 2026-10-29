
SIZE = 100
key = [0] * SIZE
left = [-1] * SIZE
right = [-1] * SIZE
height = [0] * SIZE
count = 0
root = -1

def h(i):
    return height[i] if i != -1 else 0

def new_node(value):
    global count
    i = count
    count += 1
    key[i] = value
    height[i] = 1
    return i

def update(i):
    height[i] = 1 + max(h(left[i]), h(right[i]))

def balance(i):
    return h(left[i]) - h(right[i])

def rotate_right(y):
    x = left[y]
    t = right[x]
    right[x] = y
    left[y] = t
    update(y)
    update(x)
    return x

def rotate_left(x):
    y = right[x]
    t = left[y]
    left[y] = x
    right[x] = t
    update(x)
    update(y)
    return y

def insert(node, value):
    if node == -1:
        if count >= SIZE:
            print("Tree is full")
            return -1
        return new_node(value)

    if value < key[node]:
        child = insert(left[node], value)
        if child != -1 or left[node] == -1:
            left[node] = child
    elif value > key[node]:
        child = insert(right[node], value)
        if child != -1 or right[node] == -1:
            right[node] = child
    else:
        print("Duplicate value")
        return node

    update(node)
    b = balance(node)

    if b > 1 and value < key[left[node]]:
        return rotate_right(node)

    if b < -1 and value > key[right[node]]:
        return rotate_left(node)

    if b > 1 and value > key[left[node]]:
        left[node] = rotate_left(left[node])
        return rotate_right(node)

    if b < -1 and value < key[right[node]]:
        right[node] = rotate_right(right[node])
        return rotate_left(node)

    return node

def search(value):
    i = root
    while i != -1:
        if key[i] == value:
            print("Value found")
            return
        if value < key[i]:
            i = left[i]
        else:
            i = right[i]
    print("Value not found")

def inorder(i):
    if i == -1:
        return
    inorder(left[i])
    print(key[i], end=" ")
    inorder(right[i])

def preorder(i):
    if i == -1:
        return
    print(key[i], end=" ")
    preorder(left[i])
    preorder(right[i])

def postorder(i):
    if i == -1:
        return
    postorder(left[i])
    postorder(right[i])
    print(key[i], end=" ")

while True:
    print("\n1.Insert  2.Search")
    print("3.Inorder  4.Preorder")
    print("5.Postorder  6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        old_count = count
        root = insert(root, value)
    elif choice == 2:
        search(int(input("Enter value: ")))
    elif choice == 3:
        inorder(root)
        print()
    elif choice == 4:
        preorder(root)
        print()
    elif choice == 5:
        postorder(root)
        print()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
