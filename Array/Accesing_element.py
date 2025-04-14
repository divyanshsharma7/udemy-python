import array
arr=array.array("i",[1,2,3,4,5,6])
def AccessElement(array, index):
    if index >= len(array):
        print("There is no element in this array list ")
    else:
        print(array[index])
AccessElement(arr, 3)   #index number which we want to access