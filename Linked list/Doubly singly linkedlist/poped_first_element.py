class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class CSlinkedlist:
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
            self.tail=new_node
        self.length+=1

    def popped_first(self):
        
        popped_node=self.head
        self.head=self.head.next
        self.tail.next=self.head
        popped_node.next=None
        self.length-=1
        return popped_node
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result
 

obj=CSlinkedlist()
print(obj.append(20))
print(obj.append(30))
print(obj.append(40))
print(obj.popped_first())


        

        
        
        
