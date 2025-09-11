class Treenode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

obj=Treenode("Drinks")
leftChild=Treenode("Hot")
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

inorder_traversal(obj)

