import numpy as np
array2d=np.array([[1, 2, 3], [5, 6, 7], [0, 9, 8]])
print(array2d) # it will print the 2D array
new2Darray=np.insert(array2d, 0, [[10,11,12]], axis=1)
print(new2Darray) # it will insert the new array at index 0 along axis 1


new2Darray=np.insert(array2d, 0, [[10,11,12]], axis=0)  
print(new2Darray) # it will insert the new array at index 0 along axis 0