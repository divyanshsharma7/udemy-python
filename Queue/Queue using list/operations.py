class Queue:
    def __init__(self):
        self.items=[]

    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    def enqueue(self,value):
        self.items.append(value)
        return "The element is inserted at the end of the queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the queue"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element in this queue"
        else:
            return self.items[0]
        
    def delete(self):
        self.items=None

    

obj=Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
print(obj.dequeue())
print(obj)

