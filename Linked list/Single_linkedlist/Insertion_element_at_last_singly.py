class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
class Linkedlist:
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
            self.tail=new_node
        self.length+=1
        
    def __str__(self):
        temp_node = self.head
        result=" "
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result += " ---> "
            temp_node=temp_node.next
        return result
        
   

obj=Linkedlist() 
obj.append(10)
obj.append(20)
obj.append(30)
# print(obj.head.value)
# print(obj.tail.value)
# print(obj.length)

print(obj)



