class Stack:
    def __init__(self):
        self.item=[]
    
    def is_empty(self):
        return len(self.item)==0

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        values=[str(x) for x in reversed(self.item)]
        return '\n'.join(values)
    
    def push(self,element):
        
        self.item.append(element)

    def peek(self):
         if self.is_empty():
            return "Stack is empty"
         return self.item[-1]


obj=Stack()
obj.push(10)
obj.push(20)
obj.push(30)
print(obj)
print("Peek element is : ",obj.peek())


    