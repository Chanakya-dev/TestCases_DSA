import unittest
from Searching import LinkedList, Node
class TestLinkedList(unittest.TestCase):

    # Test Case 1: Search for a node in an empty list
    def test_search_in_empty_list(self):
        ll = LinkedList()  # Create an empty linked list
        result = ll.search(10)  # Search for a key (10) in the empty list
        self.assertFalse(result)  # Expected output: False (key not found)

    # Test Case 2: Search for an existing node in the linked list
    def test_search_existing_node(self):
        ll = LinkedList()
        ll.head = Node(10)  # Add nodes to the list
        second = Node(20)
        ll.head.next = second
        second.next = Node(30)

        # Search for an existing node (20)
        result = ll.search(20)
        self.assertTrue(result)  # Expected output: True (20 is found)

    # Test Case 3: Search for a non-existing node in the linked list
    def test_search_non_existing_node(self):
        ll = LinkedList()
        ll.head = Node(10)  # Add nodes to the list
        second = Node(20)
        ll.head.next = second
        second.next = Node(30)

        # Search for a non-existing node (40)
        result = ll.search(40)
        self.assertFalse(result)  # Expected output: False (40 is not found)

    # Test Case 4: Search for the first node in the linked list
    def test_search_first_node(self):
        ll = LinkedList()
        ll.head = Node(10)  # Add a node with value 10
        second = Node(20)
        ll.head.next = second

        # Search for the first node (10)
        result = ll.search(10)
        self.assertTrue(result)  # Expected output: True (10 is found)

    # Test Case 5: Search for the last node in the linked list
    def test_search_last_node(self):
        ll = LinkedList()
        ll.head = Node(10)  # Add nodes to the list
        second = Node(20)
        ll.head.next = second
        third = Node(30)
        second.next = third

        # Search for the last node (30)
        result = ll.search(30)
        self.assertTrue(result)  # Expected output: True (30 is found)

    # Test Case 6: Search for a key that appears multiple times in the list
    def test_search_duplicate_nodes(self):
        ll = LinkedList()
        ll.head = Node(10)  # Add nodes with duplicate values
        second = Node(20)
        ll.head.next = second
        second.next = Node(20)

        # Search for the duplicate node (20)
        result = ll.search(20)
        self.assertTrue(result)  # Expected output: True (20 is found)

    # Test Case 7: Search for a key at the beginning of the linked list
    def test_search_at_beginning(self):
        ll = LinkedList()
        ll.head = Node(10)  # Add nodes to the list
        ll.head.next = Node(20)
        ll.head.next.next = Node(30)

        # Search for the first node (10)
        result = ll.search(10)
        self.assertTrue(result)  # Expected output: True (10 is found)

if __name__ == '__main__':
    unittest.main()
