class Node:
    def __init__(self, info, priority):
        self.info = info
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, node):
        for x in range(len(self.queue)):
            # Lower priority value = higher priority
            if node.priority < self.queue[x].priority:
                self.queue.insert(x, node)
                break
        else:
            # Insert at the end if it has the lowest priority
            self.queue.append(node)
        return True

    def delete(self):
        if not self.queue:
            print("Queue is empty")
            return None
        x = self.queue.pop(0)
        print("Deleted data with the given priority:", x.info, x.priority)
        return x

    def show(self):
        if not self.queue:
            print("Queue is empty")
        else:
            for x in self.queue:
                print(f"{x.info} - {x.priority}")

# Demo Run
pq = PriorityQueue()
pq.insert(Node("Task1", 3))
pq.insert(Node("Task2", 1))
pq.insert(Node("Task3", 2))
pq.insert(Node("Task4", 4))

print("Queue after insertions:")
pq.show()

pq.delete()
print("\nQueue after deletion:")
pq.show()
