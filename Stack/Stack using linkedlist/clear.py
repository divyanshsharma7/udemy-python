class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.length=0

    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        self.length+=1

    def pop(self):
        if self.top is None:
            return None
        pop_node=self.top
        self.top=self.top.next
        pop_node.next=None
        self.length-=1
        return pop_node
    
    def is_empty(self):
        return self.length==0
    
    def clear(self):
        self.top=None
        self.length=0

obj=Stack()
obj.push(10)
obj.push(20)
obj.push(30)
print(obj)
obj.clear()
print(obj)