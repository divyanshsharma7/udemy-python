
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
    
    def set_method(self,index,value):
        node=self.get(index)
        if node:
            node.value=value
            return True
        return False
        


obj=DoubleLinkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj)
obj.set_method(1,23)
print(obj)

        