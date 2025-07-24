# Singly Linked List
# Demonstrates insertion at the front of the list:
# Final list after inserting 10, 20, 30 at front: 30 -> 20 -> 10 -> None

from typing import Optional

class Node:
    def __init__(self, data):  # Corrected constructor name
        self.data = data
        self.next: Optional['Node'] = None
       
class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the front
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Print the linked list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Driver code
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_front(10)
    ll.insert_front(20)
    ll.insert_front(30)
    ll.print_list()


        

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
        