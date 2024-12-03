def demonstrate_time_complexity():
    """
    Demonstrates different time complexities using array operations
    Returns a dictionary with results of constant and linear time operations
    """
    # Initialize test data
    array = list(range(1000))  # Create an array with 1000 elements
    
    # Constant time operation O(1) - accessing element by index
    first_element = array[0]
    last_element = array[-1]
    
    # Linear time operation O(n) - searching for an element
    target = 500
    found_index = -1
    for i in range(len(array)):
        if array[i] == target:
            found_index = i
            break
    
    return {
        "constant_time_operations": {
            "first_element": first_element,
            "last_element": last_element
        },
        "linear_time_operation": {
            "found_index": found_index,
            "target_value": target
        }
    }

class SimpleArray:
    def __init__(self):
        """Initialize an empty array"""
        self.data = []
        self.size = 0
    
    def add(self, item):
        """
        Add an item to the end of the array
        Returns True if successful
        """
        self.data.append(item)
        self.size += 1
        return True
    
    def get(self, index):
        """
        Get item at specified index
        Returns None if index is invalid
        """
        if 0 <= index < self.size:
            return self.data[index]
        return None
    
    def remove(self, index):
        """
        Remove item at specified index
        Returns True if successful, False if index is invalid
        """
        if 0 <= index < self.size:
            self.data.pop(index)
            self.size -= 1
            return True
        return False
    
    def length(self):
        """Return the current size of the array"""
        return self.size
    
    def search(self, item):
        """
        Search for an item and return its index
        Returns -1 if item not found
        """
        for i in range(self.size):
            if self.data[i] == item:
                return i
        return -1