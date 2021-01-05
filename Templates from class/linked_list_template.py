class Node:
    # this is how an object of our type will be initialized
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        s = ""
        p = self.head
        while (p != None):
            s += str(p.data) + " -> "
            p = p.nextNode
        # End of list
        s += "None"
        return s
    '''Add node to end of list'''
    def append(self, n):
        pass
    '''Add node to beginning of list'''
    def prepend(self, n):
        pass
    '''Test (True/Fast) if an element in the list has value x'''
    def find(self, x):
        pass
    '''Remove an element in the list that has value x'''
    def remove(self, x):
        pass
    '''Concatinate two lists'''
    def __add__(self, other):
        pass
    '''Insert node n after index i '''
    def insert(self, i, n):
        if self.head == None:
            self.head = n
            self.tail = n
            return
        else:
            counter = 0
            while self.head != None:
                counter += 1
                if counter == i:
                    self.i.next = n
                    n.next = n.nextNode
                    break
                    
    '''Reverse the list'''
    def reverse(self):
        curNode = self.head
        while curNode != None:
            print(curNode)
            curNode =  curNode.next

        
L = LinkedList()
L.append(Node('a'))
L.append(Node('b'))
L.append(Node('c'))
L.prepend(Node('1'))
L.prepend(Node('2'))
print(L)

