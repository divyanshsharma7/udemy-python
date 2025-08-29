class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None
    
    def __str__(self):
        return str(self.value)
    
class DoubleLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node:
            result+=str(temp_node.value)
            if temp_node.next:
                result+= '<->'
            temp_node=temp_node.next
        return result
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        # Optimization: start from head or tail depending on index
        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    

    def insert(self,index,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            temp_node=self.get(index-1)
            new_node.next=temp_node.next
            new_node.prev=temp_node
            temp_node.next.prev=new_node
            new_node.prev=temp_node
            temp_node.next=new_node
            

        self.length+=1

obj=DoubleLinkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj)
obj.insert(1,50)
print(obj)
