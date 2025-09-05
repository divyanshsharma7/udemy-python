from multiprocessing import Queue
obj=Queue(maxsize=3)
obj.put(1)
print(obj.get())

#Multiprocessing modules also contain the same methods as queue modules
