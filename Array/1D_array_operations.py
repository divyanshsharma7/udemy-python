import array 
arr=array.array("i",[1,2,3,4,5])
arr.append(6) # it will add 6 at the end of the array
print(arr) # it will print the array after adding 6


arr.insert(2, 10) # it will insert 10 at index 2
print(arr) 

arr1=array.array("i",[7,8,9])
arr.extend(arr1)
print(arr) # it will add all the elements of arr1 to arr


#add items from list array using fromlist() method
list=[20,21,22]
arr.fromlist(list)
print(arr) # it will add all the elements of list to arr


#using pop method to remove the last element of the array
arr.pop()
print(arr) # it will remove the last element of the array


#using reverse method to reverse the order of the array 
arr.reverse()
print(arr) # it will reverse the order of the array


#buffer_info() method to get the size of the buffer in bytes
arr.buffer_info() # it will return the size of the buffer in bytes
print(arr.buffer_info()) 


#count() method to count the number of occurrences of an element in the array
arr.count(2) # it will count the number of occurrences of 2 in the array
print(arr.count(2)) 


#converting array to list using tolist() method
arr.tolist() # it will convert the array to list
print(arr.tolist())


#slice an element from the array using slice operator
arr[2:4]
print(arr[2:4]) # it will slice the array from index 2 to 4