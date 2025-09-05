from collections import deque

obj=deque(maxlen=3)
print(obj)

obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)  #if i will try to insert 4 elements then it will remove the first element it means it will set the size according to the given size
print(obj)
obj.popleft()
print(obj)

