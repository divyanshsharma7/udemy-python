class Node:
    def __init__(self, value):
        self.value = value
        self.next = None   # fixed (was self.head)

class CSlinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node   # circular link
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def search(self,target):
        current=self.head
        while current is not None:
            if current.value==target:
                return True
            current=current.next
            if current==self.head:
                break
        return False
            


# Testing
obj = CSlinkedlist()
obj.append(10)
obj.append(20)

print("Circular Linked List:", obj)

print("Searching element is : ",obj.search(67))
