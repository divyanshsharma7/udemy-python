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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def remove(self, index):
        prev_node=self.get(index-1)
        pop_node=prev_node.next
        prev_node.next=pop_node.next
        pop_node.next=None
        self.length-=1
        return pop_node
    
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
obj.append(20)
obj.append(30)
obj.append(40)
print(obj)
obj.remove(1)
print(obj)


        

        
        
        
