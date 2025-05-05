from LinkedList.Node import Node

class Snake(Node):
    def __init__(self,  x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __str__(self):
        return "Snake: " + self.x + " " + self.y