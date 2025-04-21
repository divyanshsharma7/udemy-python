my_dict = {
    "Name": "Divyansh",
    "Age": 19,
    "Address": "Ambala"
}

def searching_element(d):
    for value in d.values():
        if "Divyansh" == value:
            return True
    return False

print(searching_element(my_dict))
