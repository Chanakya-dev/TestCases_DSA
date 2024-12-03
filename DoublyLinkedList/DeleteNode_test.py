import unittest
from DeleteNode import DoublyLinkedList
class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        # Initialize a doubly linked list and add sample nodes
        self.dll = DoublyLinkedList()
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)

    def test_delete_head_node(self):
        # Test deletion of the head node
        self.dll.delete_node(10)
        current = self.dll.head
        # Verify that the head node is now 20 and the previous pointer of the new head is None
        self.assertEqual(current.data, 20)
        self.assertIsNone(current.prev)
        self.assertEqual(current.next.data, 30)

    def test_delete_intermediate_node(self):
        # Test deletion of an intermediate node
        self.dll.delete_node(20)
        current = self.dll.head
        # Verify that node 20 is deleted and node 30 is now the next of the head node
        self.assertEqual(current.next.data, 30)
        self.assertEqual(current.next.prev.data, 10)

    def test_delete_last_node(self):
        # Test deletion of the last node
        self.dll.delete_node(30)
        current = self.dll.head
        # Verify that the last node (30) is deleted and None is the next of node 20
        self.assertIsNone(current.next)

    def test_delete_non_existent_node(self):
        # Test trying to delete a non-existent node
        self.dll.delete_node(40)
        current = self.dll.head
        # Verify that the list remains unchanged
        self.assertEqual(current.data, 10)
        self.assertEqual(current.next.data, 20)
        self.assertEqual(current.next.next.data, 30)

    def test_delete_from_empty_list(self):
        # Test deleting from an empty list
        empty_dll = DoublyLinkedList()
        empty_dll.delete_node(10)
        # Check that the list is still empty (head should be None)
        self.assertIsNone(empty_dll.head)

if __name__ == '__main__':
    unittest.main()
