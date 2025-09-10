class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

obj=TreeNode("Drinks")
leftChild=TreeNode("Hot")
rightChild=TreeNode("Cold")
obj.leftChild=leftChild
obj.rightChild=rightChild

def preorder_traversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorder_traversal(rootNode.leftChild)
    preorder_traversal(rootNode.rightChild)

preorder_traversal(obj)