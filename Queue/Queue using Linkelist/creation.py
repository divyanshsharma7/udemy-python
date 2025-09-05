class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)
    
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        temp_node=self.head
        while temp_node:
            yield temp_node
            temp_node=temp_node.next

class Queue:
    def __init__(self):
        self.linkedlist=Linkedlist()

    
    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def enqueue(self,value):
        new_node=Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head=new_node
            self.linkedlist.tail=new_node
        else:
            self.linkedlist.tail.next=new_node
            self.linkedlist.tail=new_node

        
            

obj=Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
print(obj)

    

