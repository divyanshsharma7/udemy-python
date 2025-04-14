import array
arr=array.array("i", [1,34,23,56,78,89])
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index]==target:
            return index
    return -1
print(linear_search(arr, 34))  # it will return the index of the element 
print(linear_search(arr, 100)) # -1 means not found