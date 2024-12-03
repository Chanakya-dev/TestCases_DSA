import unittest
from DeleteNode import Node, CircularLinkedList  # Adjust import path as necessary

class TestCircularLinkedList(unittest.TestCase):
    def setUp(self):
        """Set up a circular linked list for each test."""
        self.cll = CircularLinkedList()

        # Create nodes and link them for a circular linked list
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)

        self.cll.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node1  # Making it circular

    def test_delete_head(self):
        """Test deleting the head node."""
        self.cll.delete_node(10)
        self.assertEqual(self.cll.head.data, 20)  # Head should now be 20
        self.assertEqual(self.cll.head.next.data, 30)  # Next node after head is 30
        self.assertEqual(self.cll.head.next.next.data, 20)  # List remains circular

    def test_delete_non_head(self):
        """Test deleting a non-head node."""
        self.cll.delete_node(30)
        self.assertEqual(self.cll.head.data, 10)  # Head remains unchanged
        self.assertEqual(self.cll.head.next.data, 20)  # Next node is 20
        self.assertEqual(self.cll.head.next.next.data, 10)  # List remains circular

    def test_delete_non_existent_node(self):
        """Test attempting to delete a non-existent node."""
        self.cll.delete_node(40)  # Node 40 does not exist
        self.assertEqual(self.cll.head.data, 10)  # Head remains unchanged
        self.assertEqual(self.cll.head.next.data, 20)  # Structure remains intact
        self.assertEqual(self.cll.head.next.next.data, 30)  # Structure remains intact

    def test_delete_only_node(self):
        """Test deleting the only node in a single-node list."""
        single_node_cll = CircularLinkedList()
        node = Node(100)
        single_node_cll.head = node
        node.next = node  # Single-node circular linked list

        single_node_cll.delete_node(100)  # Delete the only node
        self.assertIsNone(single_node_cll.head)  # List should now be empty

    def test_delete_head_in_two_node_list(self):
        """Test deleting the head in a two-node circular linked list."""
        two_node_cll = CircularLinkedList()
        node1 = Node(10)
        node2 = Node(20)
        two_node_cll.head = node1
        node1.next = node2
        node2.next = node1  # Circular linking

        two_node_cll.delete_node(10)  # Delete the head
        self.assertEqual(two_node_cll.head.data, 20)  # Head should now be 20
        self.assertEqual(two_node_cll.head.next.data, 20)  # Single node points to itself

    def test_delete_tail_in_two_node_list(self):
        """Test deleting the tail in a two-node circular linked list."""
        two_node_cll = CircularLinkedList()
        node1 = Node(10)
        node2 = Node(20)
        two_node_cll.head = node1
        node1.next = node2
        node2.next = node1  # Circular linking

        two_node_cll.delete_node(20)  # Delete the tail
        self.assertEqual(two_node_cll.head.data, 10)  # Head remains unchanged
        self.assertEqual(two_node_cll.head.next.data, 10)  # Single node points to itself

if __name__ == "__main__":
    unittest.main()
