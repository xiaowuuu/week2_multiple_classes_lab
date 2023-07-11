class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

# help the queue get person from Person class
    def add_to_queue(self, person):
        self.queue.append(person)

# remove all people from the queue
    def clear(self):
        self.queue.clear()

    def queue_length(self):
        return len(self.queue)
    