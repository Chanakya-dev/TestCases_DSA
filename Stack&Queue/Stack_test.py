import unittest
from Stack import push, pop
class TestStackOperations(unittest.TestCase):
    
    # Test Case 1: Test pushing elements into the stack
    def test_push_elements(self):
        global stack, top
        stack = [None] * 3  # Reinitialize the stack for each test case
        top = -1
        
        # Push 10, 20, and 30 into the stack
        push(10)
        self.assertEqual(stack, [10, None, None])
        self.assertEqual(top, 0)
        
        push(20)
        self.assertEqual(stack, [10, 20, None])
        self.assertEqual(top, 1)
        
        push(30)
        self.assertEqual(stack, [10, 20, 30])
        self.assertEqual(top, 2)
        
    # Test Case 2: Test pushing when the stack is full
    def test_push_when_full(self):
        global stack, top
        stack = [None] * 3  # Reinitialize the stack for each test case
        top = 2  # Set to the last valid index
        
        # Try to push 40 into the full stack
        push(40)
        self.assertEqual(stack, [10, 20, 30])
        self.assertEqual(top, 2)
        
    # Test Case 3: Test popping elements from the stack
    def test_pop_elements(self):
        global stack, top
        stack = [10, 20, 30]  # Set the stack with elements
        top = 2  # Set the top pointer
        
        # Pop the top element (30)
        pop()
        self.assertEqual(stack, [10, 20, None])
        self.assertEqual(top, 1)
        
        # Pop the next element (20)
        pop()
        self.assertEqual(stack, [10, None, None])
        self.assertEqual(top, 0)
        
        # Pop the last element (10)
        pop()
        self.assertEqual(stack, [None, None, None])
        self.assertEqual(top, -1)
        
    # Test Case 4: Test popping when the stack is empty
    def test_pop_when_empty(self):
        global stack, top
        stack = [None] * 3  # Reinitialize the stack for each test case
        top = -1  # Set to the empty state
        
        # Try to pop from the empty stack
        pop()
        self.assertEqual(stack, [None, None, None])
        self.assertEqual(top, -1)
        
    # Test Case 5: Test pushing after popping elements
    def test_push_after_pop(self):
        global stack, top
        stack = [None] * 3  # Reinitialize the stack for each test case
        top = -1
        
        # Push 10, 20, 30 into the stack
        push(10)
        push(20)
        push(30)
        
        # Pop all elements
        pop()  # Pop 30
        pop()  # Pop 20
        pop()  # Pop 10
        
        # Push 40 after popping
        push(40)
        self.assertEqual(stack, [40, None, None])
        self.assertEqual(top, 0)
        
if __name__ == '__main__':
    unittest.main()
