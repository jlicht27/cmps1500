class Node:
    # this is how an object of our type will be initialized
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = None
​
    # this function defines how to convert our type to a string
    def __str__(self):
        return str(self.data)
​
    def print_list_pretty(self):
        p = self
        while (p != None):
            print (p.data, "->", end="")
            p = p.next
        # End of list
        print ("None")
​
​
​
#Write a function that removes the first element from a list
def removeFirst(L):
     return L.next
​
​
# Add a new item to L by adding it to the front of the list
def addFirst(L, x):
    L.insert(0,x)
    return L
​
​
# Remove the item in L holding x
def findAndRemove(L, x):
    for i in L:
        if i == x:
            
​
​
#Write a function that returns the value for an element at index i
def getValue(L, i):
    for j in L:
        if j == i:
            #something
        
    
​
 
        
# an example of how to set up a linked structure using our Node data type
A = Node('a')
A.next = Node('b')
A.next.next = Node('c')
A.next.next.next = Node('d')
A.print_list_pretty()
​
B = Node('a')
t = Node('b')
B.next = t
q = Node('c')
t.next = q
r = Node('d')
q.next = r
B.print_list_pretty()
