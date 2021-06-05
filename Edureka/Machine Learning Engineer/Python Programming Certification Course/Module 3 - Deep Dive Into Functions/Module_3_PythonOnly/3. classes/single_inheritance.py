"""
Super=Base=Parent
Sub = Derived= Child
"""

# single inheritance

class Vehicle:
    def __init__(self, a, b, c):
        self.brand = a
        self.color = b
        self.no_of_tyres = c

    def apply_brake(self):
        # some logic for applying brake
        print("Brake applied")


class Car(Vehicle):
    pass


car_obj = Car("honda", 'black', 4)

print(car_obj.brand)
car_obj.apply_brake()
