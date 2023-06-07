import Queue as q

my_queue = q.Queue()

my_queue.insert(4)
my_queue.insert(10)
my_queue.insert(-8)

print(my_queue)

print("Removed Item: ", my_queue.remove())

print("First Item in Queue: ", my_queue.peek())

print(my_queue)

my_queue.insert(99)
print("Added new item: ", my_queue)
