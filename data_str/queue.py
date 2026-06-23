# FIFO First In First Out

# Enqueue (kuyruğa ekle)
# Dequeue (kuyruktan çıkar)

queue = []

queue.append(10)
print(queue)

queue.append(20)
queue.append(50)

print(queue)

first_element = queue.pop(0)
print(first_element)

front = queue[0]
print(front)

if len(queue) == 0:
    print("Queue is empty!")
