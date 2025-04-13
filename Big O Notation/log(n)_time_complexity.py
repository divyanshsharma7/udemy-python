def max_number(arr):
    arr=[1,2,3,4,5,6]
    big_no=arr[0]
    for i in range(1, len(arr)):
        if arr[i]>big_no:
            big_no=arr[i]   
    print(big_no)
    
max_number([1,2,3,4,5,6])

    