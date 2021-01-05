
class Phonebook():
    def __init__(self):
        self.phonebook = {'Bob': 72345, 'Sally': 7100, 'John': 79999}

    def isNamePresent(self, name):
        if name in self.phonebook.keys():
            return True
        else:
            return False

    def numberFor(self, name):
        a = self.isNamePresent(name)
        if a == True:
            return self.phonebook[name]
        else:
            return -1
        





    
book = Phonebook()

#print(book.isNamePresent('Bob'))


print(book.numberFor('Bob'))
