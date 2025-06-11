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
    def insert(self,index, value):
        new_node=Node(value)
        temp_node=self.head
        for _ in range(index-1):
            temp_node=temp_node.next
        new_node.next=temp_node.next
        temp_node.next=new_node
        self.length+=1
obj=Linkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj)
obj.insert(1,15)
print(obj)



# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
        
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.length=0
#     def append(self,value):
#         new_node=Node(value)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             self.tail=new_node
#         self.length+=1
    
#     def __str__(self):  
#         temp_node=self.head
#         result=" "
#         while temp_node is not None:
#             result+=str(temp_node.value)
#             if temp_node.next is not None:
#                 result+="--->"
#             temp_node=temp_node.next
#         return result
#     def insert(self,index,value):
#         new_node=Node(value)
#         temp_node=self.head
#         for _ in range(index-1):
#             temp_node=temp_node.next
#         new_node.next=temp_node.next
#         temp_node.next=new_node
#         self.length+=1
# obj=Linkedlist()
# obj.append(10)
# obj.append(20)
# obj.append(30)
# print(obj)
# obj.insert(1, 15)
# print(obj)           
        
        