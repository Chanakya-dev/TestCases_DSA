import unittest
from NodeatEnd import CircularLinkedList  # Adjust the import according to your file structure

class TestCircularLinkedList(unittest.TestCase):
    
    def setUp(self):
        # Initialize a new circular linked list before each test
        self.cll = CircularLinkedList()

    def test_add_last_to_empty_list(self):
        # Add a node to an empty circular linked list
        self.cll.add_last(10)
        self.assertEqual(self.cll.head.data, 10)
        self.assertEqual(self.cll.head.next, self.cll.head)  # The next should point to the head itself

    def test_add_last_to_non_empty_list(self):
        # Add nodes to a non-empty circular linked list
        self.cll.add_last(10)
        self.cll.add_last(20)
        self.assertEqual(self.cll.head.data, 10)  # Head should remain the same
        self.assertEqual(self.cll.head.next.data, 20)  # The next node should be 20
        self.assertEqual(self.cll.head.next.next, self.cll.head)  # The last node should point back to the head

    def test_add_multiple_nodes(self):
        # Add multiple nodes and verify the structure
        self.cll.add_last(10)
        self.cll.add_last(20)
        self.cll.add_last(30)
        self.cll.add_last(40)

        # Check the circular structure of the list
        current = self.cll.head
        nodes = []
        while True:
            nodes.append(current.data)
            current = current.next
            if current == self.cll.head:
                break
        self.assertEqual(nodes, [10, 20, 30, 40])  # The list should be in the order of insertion

    def test_empty_list(self):
        # Check if the list is empty initially
        self.assertIsNone(self.cll.head)

    def test_single_node_in_list(self):
        # Add a single node and verify circular behavior
        self.cll.add_last(100)
        self.assertEqual(self.cll.head.data, 100)
        self.assertEqual(self.cll.head.next, self.cll.head)  # The node should point to itself

if __name__ == "__main__":
    unittest.main()
