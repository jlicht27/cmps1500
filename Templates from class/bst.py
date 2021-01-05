class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def print_tree(T, indent=0):
    if T != None:
        print_tree(T.right, indent+4)
        print (indent*" ", T.data)
        print_tree(T.left, indent+4)
               
# find the minimum element of a binary search tree
def tree_min(T):
    if T != None:
        current = T
        while (current.left != None):
           current = current.left
        return current.data
    else:
        return None

# find the maximum element of a non-empty binary search tree
def tree_max(T):
    if T != None:
        current = T
        while (current.right != None):
            current = current.right
        return current.data
    else:
        return None
    
# recursive tree_max
def tree_max_rec(T):
    if T != None:
        if(T.right == None):
            return T.data
        return tree_max_rec(T.right)
    else:
        return None

#Return True if x is in T, otherwise false
#Hint: easiest to do recursively
def find(T,x):
    if(T == None):
        return False
    if(T.data == x):
        return True
    if(x < T.data):
        return find(T.left, x)
    else:
        return find(T.right, x)

#Insert new node with value x into tree
#Hint: Find the right "None" spot
def insert(T,x):
    if(x <= T.data):
        if(T.left == None):
            T.left = TreeNode(x)
        else:
            insert(T.left, x)
    else:
        if(T.right == None):
            T.right = TreeNode(x)
        else:
            insert(T.right, x)
      

#Inorder Traversal: left, then root, then right
#Hint: easiest to do recursively
def print_inorder(T):
    if T!=None:
        print_inorder(T.left)
        print(T.data)
        print_inorder(T.right)

#Preorder Traversal: root, then left, then right
#Hint: easiest to do recursively
def print_preorder(T):
    if T!=None:
        print(T.data)
        print_preorder(T.left)
        print_preorder(T.right)

#Postorder Traversal: left, then right, then root
#Hint: easiest to do recursively
def print_postorder(T):
    if T!=None:
        print_postorder(T.left)
        print_postorder(T.right)
        print(T.data)
        
#Return total number of nodes in the tree
#Hint: easiest to do recursively
def size(T):
    pass


root = TreeNode(50)
insert(root, 42)
insert(root, 55)
insert(root, 65)
insert(root, 46)
insert(root, 52)
insert(root, 20)

##root.left = TreeNode(42)
##root.right = TreeNode(55)
##root.right.right= TreeNode(65)
##root.left.right = TreeNode(46)
##root.right.left = TreeNode(52)
##root.left.left = TreeNode(20)

print_inorder(root)
print_tree(root)

print ("Minimum: ", tree_min(root))
print ("Minimum, empty tree: ", tree_min(None))
print ("Maximum: ", tree_max(root))
print ("Maximum, empty tree: ", tree_max(None))
print ("Max_rec: ", tree_max_rec(root))
print ("Max_rec, empty tree:  ", tree_max_rec(None))

