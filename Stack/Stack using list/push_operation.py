class Stack:
    def __init__(self):
        self.item=[]

    def push(self,element):
        self.item.append(element)

obj=Stack()
obj.push(10)
obj.push(20)
obj.push(30)
print(obj.item)
