import unittest
from NodeatBegin import CircularLinkedList
class TestCircularLinkedList(unittest.TestCase):
    def setUp(self):
        """Set up a circular linked list for each test."""
        self.cll = CircularLinkedList()

    def test_add_first_empty_list(self):
        """Test adding the first node to an empty circular linked list."""
        self.cll.add_first(10)
        self.assertEqual(self.cll.head.data, 10)  # Head should be the new node
        self.assertEqual(self.cll.head.next, self.cll.head)  # Single node should point to itself

    def test_add_first_multiple_nodes(self):
        """Test adding multiple nodes to the circular linked list."""
        self.cll.add_first(10)
        self.cll.add_first(20)
        self.cll.add_first(30)

        self.assertEqual(self.cll.head.data, 30)  # Head should be the last added node
        self.assertEqual(self.cll.head.next.data, 20)  # Next node should be 20
        self.assertEqual(self.cll.head.next.next.data, 10)  # Following node should be 10
        self.assertEqual(self.cll.head.next.next.next, self.cll.head)  # Circular linkage

    def test_display_empty_list(self):
        """Test displaying an empty list."""
        # Capturing the printed output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        self.cll.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "List is empty.")

    def test_display_non_empty_list(self):
        """Test displaying a non-empty circular linked list."""
        self.cll.add_first(10)
        self.cll.add_first(20)
        self.cll.add_first(30)

        # Capturing the printed output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        self.cll.display()
        sys.stdout = sys.__stdout__

        expected_output = "30 -> 20 -> 10 -> (Back to head)"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()
