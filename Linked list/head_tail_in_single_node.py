class linkedlist:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node