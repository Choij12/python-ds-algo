# Stack and Queue
- Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Challenge
**Features**
#### Node
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
#### Stack
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
- This object should be aware of a default empty value assigned to top when the stack is created.
The class should contain the following methods:
##### push
- Arguments: value
- adds a new node with that value to the top of the stack with an O(1) Time performance.
##### pop
- Arguments: none
- Returns: the value from node from the top of the stack
- Removes the node from the top of the stack
- Should raise exception when called on empty stack
##### peek
- Arguments: none
- Returns: Value of the node located at the top of the stack
- Should raise exception when called on empty stack
##### is empty
- Arguments: none
- Returns: Boolean indicating whether or not the stack is empty.
#### Queue
- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
- This object should be aware of a default empty value assigned to front when the queue is created.
- The class should contain the following methods:
##### enqueue
- Arguments: value
- adds a new node with that value to the back of the queue with an O(1) Time performance.
##### dequeue
- Arguments: none
- Returns: the value from node from the front of the queue
- Removes the node from the front of the queue
- Should raise exception when called on empty queue
##### peek
- Arguments: none
- Returns: Value of the node located at the front of the queue
- Should raise exception when called on empty stack
##### is empty
- Arguments: none
- Returns: Boolean indicating whether or not the queue is empty

## API

##### Stack
- `push` - Puts new nodes onto the stack.
- `pop` - Remove nodes from stack.
- `peek` - When you peek you will view the value of the top Node in the stack.
- `is_empty` - checks if stack is empty and returns a boolean value.

#####  Queue
- `enqueue` - Puts new nodes into the queue.
- `dequeue` - Remove nodes from stack front of the queue.
- `peek` - When peek is called you will view the value of the front Node in the queue.
- `is_empty` - checks if queue is empty and returns a boolean value.

## Approach & Efficiency
- Time Big 0(1)
- Space Big0(1)
