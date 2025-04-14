import array
arr=array.array("i", [1,2,3,4,5,6])
def search_element(array, index):
    if index >= len(array):
        print("Item is not found ")
    else:
        print(array[index])

search_element(arr, 5)