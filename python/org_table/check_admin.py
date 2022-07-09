admin = "maayan"
passwrd = "1234"
 
#check admin
def check_admin():
    """Check if username and pwd match, return true or false after 5 tries
    (admin: maayan, pwd: 1234)
    """
    for i in range(5):
        check_name = input("whats your username?")
        if check_name == admin:
            check_pwd = input("what s your password?")
            if check_pwd == passwrd:
                return True
            else:
                print("your password is incorrect, please enter again")
                continue
        else:
            print("your username is incorrect, please enter again")
            continue
    return False
