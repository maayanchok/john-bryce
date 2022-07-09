from datetime import date as dt
import random
#import org_table.check_admin as a
#import org_table.dict_operator as c

list_of_adds = []
def add_to_dict():
    """this function adds items to a dictionary, you can choose
        how many keys"""
    new_dict = {}
    num_item = int(input("how many items do you want to add?"))
    for i in range(num_item):
        your_key = input("What is the key you want to add?")
        your_value = convert_date()
        new_dict[your_key] = your_value
    list_of_adds.append(new_dict)
    return list_of_adds

def convert_date():
    task_date = input('Enter a date in YYYY-MM-DD format')
    year, month, day = map(int, task_date.split('-'))
    your_date = dt(year, month, day)
    return your_date

def search_in_dict(list_of_adds):
    search = input(f"What are you looking for?")
    for your_dict in list_of_adds:
        for key in your_dict:
            if search == key:
                print(key,your_dict[search])


 
answer = ""
while answer!="5":
    answer = input("""
 
        TASK MANAGMENT
    _______________________
    What do you want to do?
    _______________________
 
    1. Add new task
    2. Search for task
    3. Get list os tasks
    4. Save tasks
    5. Quit
    _______________________
    """)
    if answer == "1":
        add_to_dict()
    
    if answer == "2":
        search_in_dict(list_of_adds)

    if answer == "3":
        print(list_of_adds)
 