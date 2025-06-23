class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def get_size(self):
        if self.is_empty():
            return 0
        return (self.rear - self.front + self.capacity) % self.capacity + 1

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]


q = CircularQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.peek())
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
print(q.get_size())
print(q.is_full())
print(q.dequeue())
print(q.dequeue())
print(q.get_size())
print(q.is_empty())
