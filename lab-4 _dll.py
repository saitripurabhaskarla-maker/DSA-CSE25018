class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        print("Node inserted at beginning.")

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Node inserted at end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

        print("Node inserted at end.")

    # Insert at a position
    def insert_position(self, data, position):
        if position <= 0:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Position does not exist.")
                return
            temp = temp.next

        if temp is None:
            print("Position does not exist.")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print("Node inserted at position", position)

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print("Deleted:", temp.data)

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        if temp.next is None:
            print("Deleted:", temp.data)
            self.head = None
            return

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

        print("Deleted:", temp.data)

    # Delete from a position
    def delete_position(self, position):
        if self.head is None:
            print("List is empty.")
            return

        if position <= 0:
            print("Invalid position.")
            return

        if position == 1:
            self.delete_beginning()
            return

        temp = self.head

        for i in range(1, position):
            if temp is None:
                print("Position does not exist.")
                return
            temp = temp.next

        if temp is None:
            print("Position does not exist.")
            return

        temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        print("Deleted:", temp.data)

    # Display forward
    def display_forward(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Forward:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("NULL")

    # Display backward
    def display_backward(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        print("Backward:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("NULL")

    # Search
    def search(self, value):
        temp = self.head
        position = 1

        while temp is not None:
            if temp.data == value:
                print("Element found at position:", position)
                return

            temp = temp.next
            position += 1

        print("Element not found.")

    # Update
    def update(self, position, new_data):
        if self.head is None:
            print("List is empty.")
            return

        if position <= 0:
            print("Invalid position.")
            return

        temp = self.head

        for i in range(1, position):
            if temp is None:
                print("Position does not exist.")
                return
            temp = temp.next

        if temp is None:
            print("Position does not exist.")
            return

        old_data = temp.data
        temp.data = new_data

        print("Updated", old_data, "to", new_data)

    # Count nodes
    def count(self):
        temp = self.head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)


# MAIN PROGRAM

dll = DoublyLinkedList()

while True:

    print("\n========== DOUBLY LINKED LIST ==========")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Display Forward")
    print("8. Display Backward")
    print("9. Search")
    print("10. Update")
    print("11. Count Nodes")
    print("12. Exit")
    print("========================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        dll.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        dll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        dll.insert_position(data, position)

    elif choice == 4:
        dll.delete_beginning()

    elif choice == 5:
        dll.delete_end()

    elif choice == 6:
        position = int(input("Enter position to delete: "))
        dll.delete_position(position)

    elif choice == 7:
        dll.display_forward()

    elif choice == 8:
        dll.display_backward()

    elif choice == 9:
        value = int(input("Enter value to search: "))
        dll.search(value)

    elif choice == 10:
        position = int(input("Enter position to update: "))
        new_data = int(input("Enter new value: "))
        dll.update(position, new_data)

    elif choice == 11:
        dll.count()

    elif choice == 12:
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
