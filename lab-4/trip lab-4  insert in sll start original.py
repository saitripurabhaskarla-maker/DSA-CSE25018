
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    # Insert at end
    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    # Insert at specific index
    def insert_index(self, index, data):
        if index < 0 or index > self.count():
            print("Invalid index")
            return

        if index == 0:
            self.insert_begin(data)
            return

        new = Node(data)
        temp = self.head

        for i in range(index - 1):
            temp = temp.next

        new.next = temp.next
        temp.next = new

    # Delete at beginning
    def delete_at_start(self):
        if self.head is None:
            print("No data to delete")
        else:
            print("Deleted value =", self.head.data)
            self.head = self.head.next

    # Delete at end
    def delete_at_end(self):
        if self.head is None:
            print("No data to delete")

        elif self.head.next is None:
            print("Deleted value =", self.head.data)
            self.head = None

        else:
            temp = self.head

            while temp.next.next:
                temp = temp.next

            print("Deleted value =", temp.next.data)
            temp.next = None

    # Delete specific value
    def delete_at_specific(self, value):
        if self.head is None:
            print("No data to delete")
            return

        if self.head.data == value:
            print("Deleted value =", self.head.data)
            self.head = self.head.next
            return

        temp = self.head

        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not present")
        else:
            print("Deleted value =", temp.next.data)
            temp.next = temp.next.next

    # Count nodes
    def count(self):
        c = 0
        temp = self.head

        while temp:
            c += 1
            temp = temp.next

        return c

    # Display
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

sll = SinglyLinkedList()
n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

# Check size
if len(arr) != n:
    print("Number of elements entered is not equal to n")
else:

    # Convert array into linked list
    for value in arr:
        sll.insert_end(value)

    print("\nInitial Linked List:")
    sll.display()

while True:

    print("\n----- SINGLY LINKED LIST -----")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at specific index")
    print("4. Delete at beginning")
    print("5. Delete at end")
    print("6. Delete specific value")
    print("7. Count nodes")
    print("8. Display")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        sll.insert_begin(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        sll.insert_end(data)

    elif choice == 3:
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        sll.insert_index(index, data)

    elif choice == 4:
        sll.delete_at_start()

    elif choice == 5:
        sll.delete_at_end()

    elif choice == 6:
        value = int(input("Enter value to delete: "))
        sll.delete_at_specific(value)

    elif choice == 7:
        print("Number of nodes =", sll.count())

    elif choice == 8:
        sll.display()

    elif choice == 9:
        print("Program ended")
        break

    else:
        print("Invalid choice")
