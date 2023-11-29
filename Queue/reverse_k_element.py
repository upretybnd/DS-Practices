'#reverse k element in a queue'

class Queue:
    def __init__(self):
        self.queue = []

    def addqueue(self, item):
        self.queue.append(item)

    def removequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def reverse_first_k(self, k):
        if k > 0 and k <= self.size():
            temp_stack = []
            for _ in range(k):
                temp_stack.append(self.removequeue())
            while temp_stack:
                self.addqueue(temp_stack.pop())
            for _ in range(self.size() - k):
                self.addqueue(self.removequeue())


new_queue = Queue()

new_queue.addqueue(5)
new_queue.addqueue(2)
new_queue.addqueue(7)
new_queue.addqueue(6)
new_queue.addqueue(1)

print("Original Queue:", new_queue.queue)

k = 2
new_queue.reverse_first_k(k)

print(f"Queue after reversing first {k} elements:", new_queue.queue)
