class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            self.head = self.head.next
            temp.next = self.head

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next.next != self.head:
                temp = temp.next

            temp.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break

        print()


cll = CircularLinkedList()

while True:
    print("\n--- Circular Linked List ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Delete from End")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        cll.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        cll.insert_end(data)

    elif choice == 3:
        cll.delete_beginning()

    elif choice == 4:
        cll.delete_end()

    elif choice == 5:
        cll.display()

    elif choice == 6:
        break

    else:
        print("Invalid choice")
