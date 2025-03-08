class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_node_beginning(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def add_node_end(self, value):
        self.add_node(value)

    def add_node_between(self, value, pos):
        node = Node(value)
        if self.head is None or pos == 1:
            self.add_node_beginning(value)
        else:
            current = self.head
            count = 1
            while current.next is not None and count < pos - 1:
                current = current.next
                count += 1
            node.next = current.next
            current.next = node
            if node.next is None:  # If node is added at the end
                self.tail = node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

if __name__ == '__main__':
    linked_list = LinkedList()
    while True:
        print("\n1. Add node to linked list")
        print("2. Add node to the beginning")
        print("3. Add node in between")
        print("4. Add node at the end")
        print("5. Display the linked list")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the data: "))
            linked_list.add_node(value)
        elif choice == 2:
            value = int(input("Enter the data: "))
            linked_list.add_node_beginning(value)
        elif choice == 3:
            value = int(input("Enter the data: "))
            pos = int(input("Enter the position to insert: "))
            linked_list.add_node_between(value, pos)
        elif choice == 4:
            value = int(input("Enter the data: "))
            linked_list.add_node_end(value)
        elif choice == 5:
            linked_list.display()
        elif choice == 6:
            break
        else:
            print("Invalid choice, please try again.")
