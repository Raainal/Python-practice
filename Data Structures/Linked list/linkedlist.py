class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def menu():
    ll = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Insert at end")
        print("2. Insert at beginning")
        print("3. Delete node")
        print("4. Search")
        print("5. Display")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data to insert at end: "))
            ll.insert_at_end(data)
        elif choice == 2:
            data = int(input("Enter data to insert at beginning: "))
            ll.insert_at_beginning(data)
        elif choice == 3:
            key = int(input("Enter data to delete: "))
            ll.delete_node(key)
        elif choice == 4:
            key = int(input("Enter data to search: "))
            found = ll.search(key)
            if found:
                print("Data found in the list.")
            else:
                print("Data not found in the list.")
        elif choice == 5:
            ll.display()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()