
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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def remove(self,index):
        pop_node=self.get(index)
        pop_node.prev.next=pop_node.next
        pop_node.next.prev=pop_node.prev
        pop_node.next=None
        pop_node.prev=None
        self.length-=1
        return pop_node

        
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node:
            result+=str(temp_node.value)
            if temp_node.next:
                result+= '<->'
            temp_node=temp_node.next
        return result

obj=DoubleLinkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj)
obj.remove(2)
print(obj)
        