import unittest
from InsertatBegin import LinkedList
class TestLinkedList(unittest.TestCase):

    # Test Case 1: Insert nodes at the beginning of an empty list
    def test_insert_empty_list(self):
        ll = LinkedList()
        ll.insert_at_beginning(10)  # Insert 10 into an empty list
        # The list should contain only the node with value 10
        self.assertEqual(ll.head.data, 10)
        self.assertIsNone(ll.head.next)  # The next pointer of the node should be None

    # Test Case 2: Insert nodes at the beginning of a non-empty list
    def test_insert_non_empty_list(self):
        ll = LinkedList()
        ll.insert_at_beginning(10)  # Insert 10
        ll.insert_at_beginning(20)  # Insert 20 at the beginning
        ll.insert_at_beginning(30)  # Insert 30 at the beginning
        # The list should now be 30 -> 20 -> 10
        self.assertEqual(ll.head.data, 30)
        self.assertEqual(ll.head.next.data, 20)
        self.assertEqual(ll.head.next.next.data, 10)
        self.assertIsNone(ll.head.next.next.next)  # The last node's next should be None

    # Test Case 3: Insert multiple nodes and verify list order
    def test_insert_multiple_nodes(self):
        ll = LinkedList()
        ll.insert_at_beginning(30)
        ll.insert_at_beginning(20)
        ll.insert_at_beginning(10)
        # The list should be 10 -> 20 -> 30
        current = ll.head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        self.assertEqual(values, [10, 20, 30])

    # Test Case 4: Insert the same element multiple times
    def test_insert_duplicate_elements(self):
        ll = LinkedList()
        ll.insert_at_beginning(10)
        ll.insert_at_beginning(10)
        ll.insert_at_beginning(10)
        # The list should be 10 -> 10 -> 10
        current = ll.head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        self.assertEqual(values, [10, 10, 10])

    # Test Case 5: Insert into a list and verify the last node's pointer is None
    def test_last_node_next_none(self):
        ll = LinkedList()
        ll.insert_at_beginning(10)  # Insert 10
        ll.insert_at_beginning(20)  # Insert 20 at the beginning
        ll.insert_at_beginning(30)  # Insert 30 at the beginning
        # The last node (with value 10) should have a next pointer as None
        current = ll.head
        while current and current.next:
            current = current.next
        self.assertIsNone(current.next)  # The next of the last node should be None

if __name__ == '__main__':
    unittest.main()
