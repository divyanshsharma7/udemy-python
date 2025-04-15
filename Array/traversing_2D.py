import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

def traversing(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
traversing(arr)