
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        

class DoubleLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node:
            result+=str(temp_node.value)
            if temp_node.next:
                result+= '<->'
            temp_node=temp_node.next
        return result
    
    def search(self,target):
        current_node=self.head
        while current_node.next is not None :
            if current_node.value==target:
                return True
            current_node=current_node.next
        return False

obj=DoubleLinkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj)
print(obj.search(10))

        