
class Car:

    def drive(self,km):
        self.km += km
        self.fuel -= km*2
    def __init__(self, fuel_amount, is_electric):
        self.fuel = fuel_amount
        self.is_electric = is_electric     
        self.km = 0
    def status(self):
        print(self.is_electric)
        print(self.fuel )
        print(self.km)

car1 = Car(15,False)
car2 = Car(8,True)

car1.drive(1)
car1.status()

