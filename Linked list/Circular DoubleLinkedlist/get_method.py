
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
    
class CircularDoublylinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        temp_node=self.head
        result= ''
        while temp_node is not None:
            result +=str(temp_node.value)
            temp_node=temp_node.next
            if temp_node==self.head:
                break
            result +=' -> '
        return result
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.head.prev=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

    def get(self, index):
        current_node=None
        if index < self.length//2:
            current_node=self.head
            for i in range(index):
                current_node=current_node.next
        else:
            current_node=self.tail
            for i in range(self.length -1, index, -1):
                current_node=current_node.prev

        return current_node

obj=CircularDoublylinkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj)
print(obj.get(0))