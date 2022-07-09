import shelve
list_of_adds = []

def add_to_dict():
    """this function adds items to a dictionary, you can choose
        how many keys"""
    new_dict = {}
    num_item = int(input("how many items do you want to add?"))
    for i in range(num_item):
        your_key = input("What is the key you want to add?")
        your_value = input("What is the value?")
        new_dict[your_key] = your_value
    list_of_adds.append(new_dict)
    return list_of_adds

def search_in_dict(list_of_dict):
    """This function gets a list of dictionaries, search for a value by its key, 
    and return the specific dict"""
    search_by = input("search by: ")
    val = input(f"What {search_by} are you looking for?")
    for your_dict in list_of_dict:
        if search_by in your_dict and val == your_dict[search_by]:
            print(your_dict)

def save_dict(list_of_dict):
    your_shelf = input("Save as:")
    stock_db = shelve.open("stock_db")
    stock_db[your_shelf] = list_of_adds
    stock_db.close()

