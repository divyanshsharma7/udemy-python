class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CSLinkedlist:
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
    
    def insert(self,index,value):
        new_node=Node(value)
        temp_node=self.head
        for _ in range(index-1):
            temp_node=temp_node.next
        new_node.next=temp_node.next
        temp_node.next=new_node
        self.length+=1
    

obj=CSLinkedlist()
obj.append(20)
obj.append(30)
obj.append(40)
print(obj)

obj.prepend(10)
print("Adding element at first: ",obj)

obj.insert(3,60)
print("After inserting elemnet: ",obj)



