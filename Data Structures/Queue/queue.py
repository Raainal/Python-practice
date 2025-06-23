class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued.")

    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty. Cannot dequeue."
        return f"{self.queue.pop(0)} dequeued."

    def front(self):
        if self.is_empty():
            return "Queue is empty."
        return f"Front item: {self.queue[0]}"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        return f"Queue: {self.queue}" if not self.is_empty() else "Queue is empty."

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.display())
print(q.front())
print(q.dequeue())
