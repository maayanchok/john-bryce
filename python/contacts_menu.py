import adress_book.admin as a
import adress_book.contacts as c
import shelve
contacts = {}
s = shelve.open("adress_book")
#if a.check_admin() == True:

answer = ""
while answer!="5":
    answer = input("""
            ADRESS BOOK
    _______________________
    What do you want to do?
    _______________________

    1. Add new contact
    2. Search contact
    3. Get list contacts
    4. Save contacts
    5. Quit
    _______________________
    """)

    if answer == "1":
        c.contacts = c.add_user()
        print(contacts)
    if answer == "2":
        c.search_user(contacts)    
    if answer == "3":
        a=1
