'''Jonathan Licht
Lab 8 part 1'''


class Node:
    def __init__(self, old, new):
        self.old = old
        self.new = new
        self.next = None
    def __str__(self):
        return str(self.old) + str(self.new)


def ADD(old, new, head):
    if head == None:
        head = Node(old, new)
        print('Added')
        return head
    else:
        temp = head
        while temp != None:
            if temp.old == old:
                print('Entry already exists')
                return head
            temp = temp.next
        newNode = Node(old, new)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        print('Added')
        return head


def MAIL(address, head):
    if head == None:
        print('Send to', address)
    else:
        return MAIL(head.new, head.next)

choice = '-1'
head = None

while choice != 'QUIT':
    choice = input('Enter \"ADD\" to add an address\n\"MAIL\" to mail to an address\n\"QUIT\" to quit\n')
    if choice == 'ADD':
        old1 = input('Enter old address: ')
        new1 = input('Enter new address: ')
        head = ADD(old1, new1, head)
    elif choice == 'MAIL':
        address1 = input('Enter location you would like to mail: ')
        MAIL(address1, head)

print('Goodbye')
