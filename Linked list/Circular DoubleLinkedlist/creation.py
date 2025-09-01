
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)

class CircularDoublelinkedlist:
 
    # def __init__(self):
    #     self.head=None
    #     self.tail=None
    #     self.length=0

    def __init__(self,value):
        new_node=Node(value)
        new_node.next=new_node
        new_node.prev=new_node
        self.head=new_node
        self.tail=new_node
        self.length=1

obj=CircularDoublelinkedlist(10)
print(obj.head.value)

    
