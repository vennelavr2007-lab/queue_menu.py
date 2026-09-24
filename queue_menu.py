queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)
queue.pop(0)
print("After deletion:", queue)
queue.append(40)
print("After insertion:", queue)

OUTPUT:
Queue: [10, 20, 30]
After deletion: [20, 30]
After insertion: [20, 30, 40]
