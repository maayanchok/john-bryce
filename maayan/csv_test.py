import random

def save_csv(users, filename):
    f = open(filename, "a")
    for name in users:
        username = name
        phone = users[name]
        f.write(f"{username},{phone}\n")
    f.close()

def make_users(num):
    user_phones = {}
    for in range(num):
        phone = f"05{random.randint(2,6)}-{random.randint(5000000,8000000)}"
        user = f"user{random.randint(1,num)}{i}"
        user