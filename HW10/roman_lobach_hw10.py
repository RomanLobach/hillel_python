# спочатку зробив клас Vehicle, подім довго думав як зробити "нормальне" наслідування.
# потім PyCharm сказав, що у Python також є super. Це супер :)
# схожий приклад колись писав на js

class Vehicle:
    def __init__(self, brand, color, max_speed):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed

    def get_info(self):
        return f'Brand: {self.brand}\nColor: {self.color}\nMax Speed: {self.max_speed} km/h'


class Car(Vehicle):
    def __init__(self, brand, color, max_speed, fuel_type):
        super().__init__(brand, color, max_speed)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}\nFuel Type: {self.fuel_type}'


class Airplane(Vehicle):
    def __init__(self, brand, color, max_speed, wingspan):
        super().__init__(brand, color, max_speed)
        self.wingspan = wingspan

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}\nWingspan: {self.wingspan} meters'


class Ship(Vehicle):
    def __init__(self, brand, color, max_speed, displacement):
        super().__init__(brand, color, max_speed)
        self.displacement = displacement

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}\nDisplacement: {self.displacement} tons'


car_init_values = {
    'brand': 'Toyota',
    'color': 'red',
    'max_speed': 200,
    'fuel_type': 'Petrol'
}

airplane_init_values = {
    'brand': 'Boeing',
    'color': 'white',
    'max_speed': 900,
    'wingspan': 45
}

ship_init_values = {
    'brand': 'Titanic',
    'color': 'black',
    'max_speed': 40,
    'displacement': 53000
}

car = Car(**car_init_values)
airplane = Airplane(**airplane_init_values)
ship = Ship(**ship_init_values)

print(f'\nCar:\n{car.get_info()}')
print(f'\nAirplane:\n{airplane.get_info()}')
print(f'\nShip:\n{ship.get_info()}')
