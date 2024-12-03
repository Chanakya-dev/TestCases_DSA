import unittest
from Search import CircularLinkedList, Node
class TestCircularLinkedList(unittest.TestCase):

    def setUp(self):
        # Initialize a circular linked list
        self.cll = CircularLinkedList()
        
        # Create nodes
        self.node1 = Node(10)
        self.node2 = Node(20)
        self.node3 = Node(30)
        
        # Link the nodes to form a circular linked list
        self.cll.head = self.node1
        self.node1.next = self.node2
        self.node2.next = self.node3
        self.node3.next = self.node1  # Points back to the head node

    def test_search_found(self):
        # Test that the search function returns True for an existing node
        self.assertTrue(self.cll.search(20))  # Node with data 20 exists

    def test_search_not_found(self):
        # Test that the search function returns False for a non-existing node
        self.assertFalse(self.cll.search(100))  # Node with data 100 does not exist

    def test_search_first_node(self):
        # Test searching for the first node (head)
        self.assertTrue(self.cll.search(10))  # Node with data 10 exists

    def test_search_last_node(self):
        # Test searching for the last node
        self.assertTrue(self.cll.search(30))  # Node with data 30 exists

    def test_empty_list(self):
        # Test the search on an empty list
        empty_cll = CircularLinkedList()
        self.assertFalse(empty_cll.search(10))  # Should return False for an empty list

if __name__ == '__main__':
    unittest.main()
