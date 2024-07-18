from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, VehicleNotStartedError

class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Not enough fuel to start")

    def move (self, distance):
            fuel_needed = self.fuel_consumption * distance
            if self.fuel >= fuel_needed:
                self.fuel -= fuel_needed
                return True
            else:
                raise NotEnoughFuel("Not enough fuel to move the distance")




'''             - доработайте базовый класс `base.Vehicle`:
                - добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
                - добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`
                - добавьте метод `start`. При вызове этого метода необходимо проверить состояние `started`. И если не `started`, то нужно проверить, что топлива больше нуля, 
                  и обновить состояние `started`, иначе нужно выкинуть исключение `exceptions.LowFuelError`
                - добавьте метод `move`, который проверяет, 
                  что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), 
                  и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel` '''
