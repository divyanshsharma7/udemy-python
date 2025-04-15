import numpy as np
array2D=np.array([[1,2,3], [5,6,7], [0,9,8]])
print(array2D) # it will print the 2D array


def access_element(array2D, row, column):
    if row>=len(array2D) or column>=len(array2D[0]):
        return "Index out of range"
    else:
        print(array2D[row][column]) # it will print the element at index [row][column]
access_element(array2D, 1, 2) # it will print the element at index [1][2] 