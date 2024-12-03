# Initialize the stack and the top pointer
stack = [None] * 3  # Stack of size 3
top = -1  # Indicates the stack is empty

# Push Operation (Adding an Element)
def push(val):
    global top
    # Check if the stack is full
    if top == len(stack) - 1:
        print("Stack is full.")  # If 'top' equals size - 1, the stack is full
        return
    # Increment the 'top' pointer
    top += 1
    # Insert the new element at the 'top' position
    stack[top] = val
    print(f"Pushed {val} into the stack.")

# Pop Operation (Removing an Element)
def pop():
    global top
    # Check if the stack is empty
    if top == -1:
        print("Stack is empty.")  # If 'top' equals -1, the stack is empty
        return
    # Store the value of the top element for printing
    popped = stack[top]
    print(f"Popped element: {popped}")
    # Set the top position in the stack array to None
    stack[top] = None
    # Decrement the 'top' pointer
    top -= 1

# Example of using the stack
push(10)  # Insert 10
push(20)  # Insert 20
push(30)  # Insert 30
push(40)  # Try to insert 40 (stack is full)

pop()  # Remove 30
pop()  # Remove 20
pop()  # Remove 10
pop()  # Try to remove another element (stack is empty)
