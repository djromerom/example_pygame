class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

    def contains(self, x, y):
        current = self.head
        while current is not None:
            if current.x == x and current.y == y:
                return True
            current = current.next
        return False