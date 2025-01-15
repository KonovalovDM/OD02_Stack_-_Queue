class Queue:
    def __init__(self):
        self.items = []

    def is_emty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()

print(queue.is_emty())

queue.enqueue("творение 1")
queue.enqueue("творение 2")
queue.enqueue("творение 3")
queue.enqueue("творение 4")
queue.enqueue("творение 5")

print(queue.is_emty())
print(queue.size())
print(queue.dequeue())
print(queue.size())
