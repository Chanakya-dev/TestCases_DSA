import unittest
from DoublyNodeatEnd import DoublyLinkedList
class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        # Initialize the doubly linked list and add sample nodes
        self.dll = DoublyLinkedList()

    def test_add_last_empty_list(self):
        # Test adding the first node to an empty list
        self.dll.add_last(10)
        # Verify that the head node is 10 and there is no next or previous node
        self.assertEqual(self.dll.head.val, 10)
        self.assertIsNone(self.dll.head.next)
        self.assertIsNone(self.dll.head.prev)

    def test_add_last_multiple_nodes(self):
        # Test adding multiple nodes to the list
        self.dll.add_last(10)
        self.dll.add_last(20)
        self.dll.add_last(30)

        # Verify the list structure: 10 <-> 20 <-> 30
        current = self.dll.head
        self.assertEqual(current.val, 10)
        self.assertEqual(current.next.val, 20)
        self.assertEqual(current.next.next.val, 30)

        # Verify previous links
        self.assertIsNone(current.prev)  # Head node has no previous
        self.assertEqual(current.next.prev.val, 10)
        self.assertEqual(current.next.next.prev.val, 20)

    def test_add_last_after_initial_nodes(self):
        # Test adding nodes after an initial node has been added
        self.dll.add_last(10)
        self.dll.add_last(20)

        # Add a new node after existing nodes
        self.dll.add_last(30)

        # Verify the structure: 10 <-> 20 <-> 30
        current = self.dll.head
        self.assertEqual(current.val, 10)
        self.assertEqual(current.next.val, 20)
        self.assertEqual(current.next.next.val, 30)

    def test_print_list(self):
        # Test printing the list
        self.dll.add_last(10)
        self.dll.add_last(20)
        self.dll.add_last(30)

        # Capture the output of print_list and verify the expected output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.dll.print_list()
        sys.stdout = sys.__stdout__

        # Verify the printed output
        self.assertEqual(captured_output.getvalue().strip(), "10 <-> 20 <-> 30")

    def test_empty_list(self):
        # Test printing an empty list (should print nothing)
        empty_dll = DoublyLinkedList()

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        empty_dll.print_list()
        sys.stdout = sys.__stdout__

        # Verify that nothing is printed
        self.assertEqual(captured_output.getvalue().strip(), "")

if __name__ == '__main__':
    unittest.main()
