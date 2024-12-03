import unittest
from DeleteNode import delete,Node,LinkedList
class TestLinkedList(unittest.TestCase):

    # Test Case 1: Delete from an Empty List
    def test_delete_empty_list(self):
        ll = LinkedList()
        ll.delete(10)  # Attempting to delete from an empty list
        self.assertIsNone(ll.head)  # The list should still be empty

    # Test Case 2: Delete the Head Node
    def test_delete_head_node(self):
        ll = LinkedList()
        ll.head = Node(10)
        ll.head.next = Node(20)
        ll.head.next.next = Node(30)
        
        ll.delete(10)  # Deleting the head node
        # The new head should be the next node, which has value 20
        self.assertEqual(ll.head.data, 20)
        self.assertEqual(ll.head.next.data, 30)

    # Test Case 3: Delete a Node in the Middle
    def test_delete_middle_node(self):
        ll = LinkedList()
        ll.head = Node(10)
        ll.head.next = Node(20)
        ll.head.next.next = Node(30)
        
        ll.delete(20)  # Deleting the middle node (20)
        # The list should be 10 -> 30 after deletion
        self.assertEqual(ll.head.next.data, 30)

    # Test Case 4: Delete the Last Node
    def test_delete_last_node(self):
        ll = LinkedList()
        ll.head = Node(10)
        ll.head.next = Node(20)
        ll.head.next.next = Node(30)
        
        ll.delete(30)  # Deleting the last node (30)
        # The list should be 10 -> 20 after deletion
        self.assertIsNone(ll.head.next.next)

    # Test Case 5: Delete a Non-Existing Node
    def test_delete_non_existing_node(self):
        ll = LinkedList()
        ll.head = Node(10)
        ll.head.next = Node(20)
        ll.head.next.next = Node(30)
        
        ll.delete(40)  # Trying to delete a node that doesn't exist
        # The list should remain unchanged
        self.assertEqual(ll.head.data, 10)
        self.assertEqual(ll.head.next.data, 20)
        self.assertEqual(ll.head.next.next.data, 30)

    # Test Case 6: Delete All Nodes
    def test_delete_all_nodes(self):
        ll = LinkedList()
        ll.head = Node(10)
        ll.head.next = Node(20)
        ll.head.next.next = Node(30)
        
        ll.delete(10)  # Deleting the first node
        ll.delete(20)  # Deleting the middle node
        ll.delete(30)  # Deleting the last node
        self.assertIsNone(ll.head)  # The list should be empty

if __name__ == '__main__':
    unittest.main()
