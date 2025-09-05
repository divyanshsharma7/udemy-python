import queue as q
obj=q.Queue(maxsize=3)

print(obj.qsize)
obj.put(10)
obj.put(20)
obj.put(30)
print(obj.qsize())
print(obj.full())
print(obj.empty())
# print(obj.get())