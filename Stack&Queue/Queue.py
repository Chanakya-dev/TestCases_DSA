# Queue Implementation

# Initialize the queue with a fixed size of 3
queue = [None] * 3  # Queue of size 3
front = 0  # Points to the front of the queue
rear = 0   # Points to the next position for insertion

# Enqueue Operation (Insertion)
def enqueue(val):
    global rear
    # Check if the queue is full
    if rear == len(queue):
        print("Queue is full.")  # If rear equals the size of the queue, it's full
        return
    # Add the new element at the rear position
    queue[rear] = val
    print(f"Enqueued {val}.")
    # Increment the rear pointer
    rear += 1

# Dequeue Operation (Deletion)
def dequeue():
    global front
    # Check if the queue is empty
    if front == rear:
        print("Queue is empty.")  # If front equals rear, the queue is empty
        return
    # Print the element being removed, which is at the front
    dequeued = queue[front]
    print(f"Dequeued element: {dequeued}")
    # Increment the front pointer to remove the element logically
    front += 1

# Test the Queue Operations
enqueue("Car 1")  # Enqueue Car 1
enqueue("Car 2")  # Enqueue Car 2
enqueue("Car 3")  # Enqueue Car 3
enqueue("Car 4")  # Try to Enqueue Car 4 (Queue is full)

dequeue()  # Dequeue Car 1
dequeue()  # Dequeue Car 2
dequeue()  # Dequeue Car 3
dequeue()  # Try to Dequeue again (Queue is empty)
