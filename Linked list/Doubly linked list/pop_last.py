# class Node:
#     def __init__(self, value):
#         self.value=value
#         self.next=None
#         self.prev=None
    
#     def __str__(self):
#         return str(self.value)
    
# class DoubleLinkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.length=0

#     def __str__(self):
#         temp_node=self.head
#         result=''
#         while temp_node:
#             result+=str(temp_node.value)
#             if temp_node.next:
#                 result+= '<->'
#             temp_node=temp_node.next
#         return result
    
#     def append(self,value):
#         new_node=Node(value)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             self.tail=new_node
#         self.length+=1

#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         # Optimization: start from head or tail depending on index
#         if index < self.length // 2:
#             temp = self.head
#             for _ in range(index):
#                 temp = temp.next
#         else:
#             temp = self.tail
#             for _ in range(self.length - 1, index, -1):
#                 temp = temp.prev
#         return temp
    

#     def pop_last(self):
#         if not self.head:
#             return None  
#         pop_node=self.tail
#         if self.length==1:
#             self.head=None
#             self.tail=None
            
#         else:
#             self.tail=self.tail.prev
#             self.tail.next=None
#             pop_node.prev=None
#         self.length-=1
#         return pop_node
        

# obj=DoubleLinkedlist()
# obj.append(10)
# obj.append(20)
# obj.append(30)
# print(obj)
# print(obj.pop_last())
# print(obj)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    

class DoubleLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' <-> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail   # ✅ FIX: maintain backward link
            self.tail = new_node
        self.length += 1

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
    
    def pop_last(self):
        if not self.head:   # empty list
            return None  

        pop_node = self.tail
        if self.length == 1:   # only one element
            self.head = None
            self.tail = None
        else:                  # multiple elements
            self.tail = self.tail.prev
            self.tail.next = None
            pop_node.prev = None

        self.length -= 1
        return pop_node


# ✅ Test
obj = DoubleLinkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj)        # 10 <-> 20 <-> 30

print(obj.pop_last())  # 30
print(obj)        # 10 <-> 20


