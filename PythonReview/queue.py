## queue data structure has a FIFO behavior -- first in, first out
## use list to implement a queue
## fifo is not very efficient because when one item is removed, all the items move one space
## use deque module to prevent that
from collections import deque

## wrap queue in a deque object
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

##remove an item using popleft()
queue.popleft()
print(queue)

##check to see if queue is empty
if not queue:  ## if queue is empty = true
    print("empty")
