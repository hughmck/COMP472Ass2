import numpy as np

class Car:
    def __init__(self, occupy_square, vert, fuel, removed, ambulance, name):
        self.occupy_square = occupy_square
        self.vert = vert #boolean is car vertical, false means horizontal
        self.fuel = fuel
        self.removed = removed
        self.ambulance = ambulance
        self.name = name

    def consume_gas(self, fuel_remaining):
        self.fuel -= fuel_remaining

    def get_fuel(self):
        return self.fuel
