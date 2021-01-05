class QueueNode:
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, x):
        n = QueueNode(x)
        if(self.head == None):
           self.head = n
           self.tail = n
        else:
            self.tail.nextNode = n
            self.tail = n
    def pop(self):
        temp = self.head.data
        self.head = self.head.nextNode
        return temp
    def __str__(self):
        s = ""
        p = self.head
        while (p != None):
            s += str(p.data) + " -> "
            p = p.nextNode
        # End of list
        s += "None"
        return s


Q = Queue()
Q.append(1)
Q.append(2)
print(Q)
print(Q.pop())
print(Q)
