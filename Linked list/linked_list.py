class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        
class Linkedlist:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
new=Linkedlist(10)
print(new.head.value)
print(new.tail.value)
print(new.length)
print(new.head.next)

        