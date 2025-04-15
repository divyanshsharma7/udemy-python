import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

def search_element(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return "Item is found at Index " +str(i)+' '+str(j)
    return "item is not found"
print(search_element(arr, 8))