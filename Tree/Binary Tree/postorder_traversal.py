class Treenode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

obj=Treenode("Drinks")
leftChild=Treenode("Hot")
tea=Treenode("Tea")
coffee=Treenode("Coffee")
leftChild.leftChild=tea
leftChild.rightChild=coffee 
rightChild=Treenode("Cold")
obj.leftChild=leftChild
obj.rightChild=rightChild

def preorder(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.leftChild)
    preorder(rootnode.rightChild)

def inorder_traversal(rootnode):
    if not rootnode:
        return
    inorder_traversal(rootnode.leftChild)
    print(rootnode.data)
    inorder_traversal(rootnode.rightChild)

def postorder_traversal(rootnode):
    if not rootnode:
        return
    postorder_traversal(rootnode.leftChild)
    postorder_traversal(rootnode.rightChild)
    print(rootnode.data)

postorder_traversal(obj)

