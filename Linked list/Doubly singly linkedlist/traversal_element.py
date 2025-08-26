class Node:
    def __init__(self,value):
        self.value=value
        self.head=None

class CSLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

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



    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1

    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.tail.next=new_node
            self.head=new_node
        self.length+=1

    def traversal(self):
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next
            if current==self.head:
                break 
            
            


obj=CSLinkedlist()
obj.append(30)
obj.append(40)
obj.append(50)
print(obj)
obj.prepend(20)
print(obj)
obj.traversal()