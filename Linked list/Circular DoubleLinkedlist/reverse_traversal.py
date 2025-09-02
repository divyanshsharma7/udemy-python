class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class Doublelinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

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
    
    def reverse_traversal(self):
        current_node=self.tail
        while current_node:
            print(current_node.value)
            current_node=current_node.prev
            if current_node is self.head:
                break

    
obj=Doublelinkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj)
obj.reverse_traversal()