#Linked List implementation
class Node:
    def init(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def init(self):
        self.head=None
        self.tail=None

    def add_node(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def add_node_beginning(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node

    def addNodeEnd(self,value):
        node=Node(value)
        if self.head is None:
            self.head = node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def display(self):
        while self.head is not None:
            print(self.head.data,end='->')
            self.head=self.head.next

if __name__=='__main__':
    object=LinkedList()
    while True:
        print("1.Add node linkedlist")
        print("2.Add node to the beginning")
        print("3.Add node in between")
        print("4.Add node at the end")
        print("5.Display the linkedlist")
        print("6.Exit")
        choice=int(input("Enter the choice:"))
        if choice==1:
            value=int(input("Enter the data:"))
            