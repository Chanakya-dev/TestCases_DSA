class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete(self, key: int) -> None:
        if self.head and self.head.data == key:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    def print_list(self) -> None:
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

# Example usage
ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)

ll.print_list()  # Output: 10 -> 20 -> 30
ll.delete(20)
ll.print_list()  # Output: 10 -> 30
ll.delete(10)
ll.print_list()  # Output: 30
ll.delete(30)
ll.print_list()  # Output: (empty list)
