'''Jonathan Licht
Lab 8 part 0'''

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
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
            p = p.next
        # End of list
        s += "None"
        return s
    def append(self, n):
        if(self.head == None):
           self.head = n
           self.tail = n
        self.tail.next = n
        self.tail = n
    def prepend(self, n):
        if(self.head == None):
           self.head = n
           self.tail = n
        n.next = self.head
        self.head = n
    
def join(head1, head2):                         
    current1 = head1
    if current1 == None:
        return head2
    while current1.next != None:
        current1 = current1.next
    current1.next = head2
    return head1





A = LinkedList()
A.append(Node('1'))
A.append(Node('2'))
A.append(Node('3'))
B = LinkedList()
B.append(Node('a'))
B.append(Node('b'))
B.append(Node('c'))


join(A.head,B.head)

print(A)

         

            
        
