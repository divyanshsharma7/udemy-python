# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
        

# class Stack:

#     def __init__(self):
#         self.top=None
#         self.length=0

#     def push(self,value):
#         new_node=Node(value)
#         new_node.next=self.top
#         self.top=new_node
#         self.length+=1

# obj=Stack()
# obj.push(10)
# obj.push(20)
# obj.push(30)
# print(obj.top.value)


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.length=0

    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        self.length+=1

obj=Stack()
obj.push(10)
obj.push(20)
obj.push(30)
print(obj.top.value)
        