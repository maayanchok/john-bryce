"""
class Humain:
    - Nom
    - Gender
    - Nationalite
    - Poids
    - Date de naissance
    - id_number
    - has_weapon

    + say_hello

class Passport:
    - Nom
    - Gender
    - Nationalite
    - Poids
    - Date de naissance
    - id_number
    - expiration_date
    - has_visa = False


Fonction: check_human(human, passport) -> True/False"""



class Human:
    def __init__(
        self, name, gender, nationality, weight, birthdate, id_number, has_weapon):
        
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.weight = weight
        self.birthdate = birthdate
        self.id_number = id_number
        self.has_weapon = False

    def say_hello(self):
        print(f"Hi")

    
class Passport:
    def __init__(self, name, gender, nationality, weight, birthdate, id_number, exp_date):
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.weight = weight
        self.birthdate = birthdate
        self.id_number = id_number
        self.exp_date = exp_date

    
human1 = Human("maayan", "f", "israel", "65", "12.07.2004", "337902811",False)
human1.say_hello()

def check_weight():
    return False
def check_exp():
    return False
def check_correspondance():
    return True


