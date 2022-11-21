

class vehicle:
    def __init__(self, kind, pos, dir):
        if type(kind) is str:
            self.kind = kind


def isVertical(car):
    return car.direction == 'vertical'

def isHorizontal(car):
    return car.direction == 'horizontal'

def useGas(car, amount):
    vehicle(car).gas -= amount

def hasGas(car):
    return vehicle(car).gas > 0

def getCarLength(car) -> int:
    if vehicle.isHorizontal():
        return int(car.end[1]) - int(car.start[1]) + 1
    elif vehicle.isVertical():
        return int(car.end[0]) - int(car.start[0]) + 1

def __str__(self) -> str:
    outputString = ''
    outputString += 'Car: ' + self.name + '\n'
    outputString += '  Start:\t' + str(self.start) + '\n'
    outputString += '  End:\t\t' + str(self.end) + '\n'
    outputString += '  Direction:\t' + self.direction + '\n'
    outputString += '  Gas:\t\t' + str(self.gas)

    return outputString
