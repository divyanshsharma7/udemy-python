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
        temp_node=self.head
        result=" "
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+="--->"
            temp_node=temp_node.next
        return result
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    
    def remove_middle(self, index):
        prev_node=self.get(index-1)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node
    
obj=Linkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)
print(obj)
print(obj.remove_middle(2))
print(obj)