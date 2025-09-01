
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)

class CircularDoublelinkedlist:
 
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

obj=CircularDoublelinkedlist()
print(obj)

    
