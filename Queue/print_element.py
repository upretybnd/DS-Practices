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

    def print_queue(self):
        for item in self.queue:
            print(item)

# Example usage:
new_queue = Queue()

new_queue.addqueue(1)
new_queue.addqueue(2)
new_queue.addqueue(3)

new_queue.print_queue()
