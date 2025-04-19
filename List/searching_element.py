list=[1,2,3,4,5]
print(list)
def search_element(list, target):
    for index in range(len(list)):
        if list[index]==target:
            return index
    return -1
target=4
print(search_element(list, target))