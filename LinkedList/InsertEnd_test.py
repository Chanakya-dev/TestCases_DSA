import unittest
from InsertEnd import LinkedList
class TestLinkedList(unittest.TestCase):

    # Test Case 1: Insert a node into an empty list
    def test_insert_into_empty_list(self):
        ll = LinkedList()
        ll.insert_at_end(10)  # Insert 10 into an empty list
        # The list should now contain only the node with value 10
        self.assertEqual(ll.head.data, 10)
        self.assertIsNone(ll.head.next)  # The next pointer of the node should be None

    # Test Case 2: Insert multiple nodes into an empty list
    def test_insert_multiple_nodes(self):
        ll = LinkedList()
        ll.insert_at_end(10)  # Insert 10 at the end
        ll.insert_at_end(20)  # Insert 20 at the end
        ll.insert_at_end(30)  # Insert 30 at the end
        # The list should now be 10 -> 20 -> 30 -> None
        current = ll.head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        self.assertEqual(values, [10, 20, 30])

    # Test Case 3: Insert node after a list with existing elements
    def test_insert_after_existing_elements(self):
        ll = LinkedList()
        ll.insert_at_end(10)  # Insert 10
        ll.insert_at_end(20)  # Insert 20 at the end
        ll.insert_at_end(30)  # Insert 30 at the end
        ll.insert_at_end(40)  # Insert 40 at the end
        # The list should now be 10 -> 20 -> 30 -> 40 -> None
        current = ll.head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        self.assertEqual(values, [10, 20, 30, 40])

    # Test Case 4: Insert a node when the list has only one element
    def test_insert_into_single_node_list(self):
        ll = LinkedList()
        ll.insert_at_end(10)  # Insert 10 into an empty list
        ll.insert_at_end(20)  # Insert 20 at the end of a single-node list
        # The list should now be 10 -> 20 -> None
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.head.next.data, 20)
        self.assertIsNone(ll.head.next.next)  # The last node's next pointer should be None

    # Test Case 5: Insert the same element multiple times
    def test_insert_duplicate_elements(self):
        ll = LinkedList()
        ll.insert_at_end(10)  # Insert 10
        ll.insert_at_end(10)  # Insert 10 again
        ll.insert_at_end(10)  # Insert 10 again
        # The list should now be 10 -> 10 -> 10 -> None
        current = ll.head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        self.assertEqual(values, [10, 10, 10])

    # Test Case 6: Insert into an empty list, then display the list
    def test_insert_and_display(self):
        ll = LinkedList()
        ll.insert_at_end(10)  # Insert 10
        ll.insert_at_end(20)  # Insert 20
        ll.insert_at_end(30)  # Insert 30
        # Capturing the output from the display method
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        ll.display()  # Expected output: 10 -> 20 -> 30 -> None
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "10 -> 20 -> 30 -> None")

if __name__ == '__main__':
    unittest.main()
