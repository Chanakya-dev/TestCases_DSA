import unittest
from NodeatEnd import CircularLinkedList  # Adjust the import path to your file structure

class TestCircularLinkedList(unittest.TestCase):

    def setUp(self):
        """Set up a new circular linked list before each test."""
        self.cll = CircularLinkedList()

    def test_add_last_to_empty_list(self):
        """Test adding a node to an empty circular linked list."""
        self.cll.add_last(10)
        self.assertEqual(self.cll.head.data, 10)  # Head should be the new node
        self.assertEqual(self.cll.head.next, self.cll.head)  # Node should point to itself

    def test_add_last_to_non_empty_list(self):
        """Test adding nodes to a non-empty circular linked list."""
        self.cll.add_last(10)
        self.cll.add_last(20)
        self.assertEqual(self.cll.head.data, 10)  # Head remains the same
        self.assertEqual(self.cll.head.next.data, 20)  # The second node's data is 20
        self.assertEqual(self.cll.head.next.next, self.cll.head)  # Last node points back to head

    def test_add_multiple_nodes(self):
        """Test adding multiple nodes and verify the circular structure."""
        self.cll.add_last(10)
        self.cll.add_last(20)
        self.cll.add_last(30)
        self.cll.add_last(40)

        # Traverse the list and collect node data to verify order
        current = self.cll.head
        nodes = []
        while True:
            nodes.append(current.data)
            current = current.next
            if current == self.cll.head:
                break
        self.assertEqual(nodes, [10, 20, 30, 40])  # Check order of insertion

    def test_empty_list(self):
        """Test the initial state of the circular linked list."""
        self.assertIsNone(self.cll.head)  # Head should be None in an empty list

    def test_single_node_in_list(self):
        """Test adding a single node and verify circular behavior."""
        self.cll.add_last(100)
        self.assertEqual(self.cll.head.data, 100)  # The single node's data
        self.assertEqual(self.cll.head.next, self.cll.head)  # The node points to itself

    def test_circular_behavior(self):
        """Verify the circular behavior after multiple insertions."""
        self.cll.add_last(1)
        self.cll.add_last(2)
        self.cll.add_last(3)

        current = self.cll.head
        for _ in range(6):  # Traverse twice the length of the list
            current = current.next
        self.assertEqual(current, self.cll.head)  # Verify it circles back to the head

if __name__ == "__main__":
    unittest.main()
