import numpy as np
import array
arr=array.array("i",[23,12,34,56,4,3])
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr==target:
            return index
    return -1
print(linear_search(arr,23))