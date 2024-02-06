class Node: 
    def __init__(self, data): 
            self.data = data 
            self.right_child = None 
            self.left_child = None 

def inorder(root_node): 
    current = root_node 
    if current is None: 
        return
    print('Opening the inorder function for node: ', current.data)
    print('Checking if there is a left child')
    if current.left_child != None:
         print('there is a left child, going to call a new inorder function')
    else:
         print('there is no left child, printing current data')
    inorder(current.left_child)
    print('==printing==') 
    print(current.data)
    print('Checking if there is a right child')
    if current.right_child != None:
         print('there is a right child, going to call a new inorder function')
    else:
         print('there is no right child, going to close this current inorder function')
    inorder(current.right_child)
    print('Closing the inorder function for node: ', current.data)

def preorder(root_node):
    current = root_node
    if current is None:
        return
    print('Opening the preorder function for node: ', current.data)
    print('==printing==') 
    print(current.data)
    print('Checking if there is a left child')
    if current.left_child != None:
         print('there is a left child, going to call a new inorder function')
    else:
         print('there is no left child')        
    preorder(current.left_child)
    print('Checking if there is a right child')
    if current.right_child != None:
         print('there is a right child, going to call a new inorder function')
    else:
         print('there is no right child, going to close this current inorder function')
    preorder(current.right_child)
    print('Closing the preorder function for node: ', current.data)

def postorder(root_node):
    current = root_node
    if current is None:
        return
    print('Opening the postorder function for node: ', current.data)
    if current.left_child != None:
        print('there is a left child, going to call a new inorder function')
    else:
        print('there is no left child')   
    postorder(current.left_child)
    print('Checking if there is a right child')
    if current.right_child != None:
        print('there is a right child, going to call a new inorder function')
    else:
        print('there is no right child, going to close this current inorder function')
    postorder(current.right_child)
    print('==printing==') 
    print(current.data)
    print('Closing the postorder function for node: ', current.data)


# Creation of a tree
n1 = Node("John")  
n2 = Node("AdamSr") 
n3 = Node("AdamJr") 
n4 = Node("Dan")
n5 = Node("Richard") 
n6 = Node("Simon")  
n1.left_child = n2 
n1.right_child = n6 
n2.left_child = n3
n2.right_child = n4
n6.left_child = n5

# Call the first function
print('===== START OF PROGRAM =====')
postorder(n1)
print('===== END OF PROGRAM =====')

