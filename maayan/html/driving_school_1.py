import json
f = open("driving.html","a")
users = []
def add_to_dict():
    """this function adds items to a dictionary, you can choose
        how many keys"""
    new_dict = {}
    num_item = int(input("how many items do you want to add?"))
    for i in range(num_item):
        your_key = input("What is the key you want to add?")
        your_value = input("What is the value?")
        new_dict[your_key] = your_value
    users.append(new_dict)
    return users

str_dict = json.dumps(add_to_dict())
f.write(str_dict)