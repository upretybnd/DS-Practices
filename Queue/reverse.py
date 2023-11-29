#Reverse element in queue
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

    def reverse(self):
        stack = []
        while not self.is_empty():
            stack.append(self.removequeue())

        while stack:
            self.addqueue(stack.pop())


new_queue = Queue()

new_queue.addqueue(5)
new_queue.addqueue(9)
new_queue.addqueue(13)

print("Original Queue:", new_queue.queue)

new_queue.reverse()

print("Reversed Queue:", new_queue.queue)
