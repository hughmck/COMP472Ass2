import numpy as np

from vehicle import vehicle


def parseStringToMap(grid, str):
        def split(word):
            return list(word)

        def splitString(a, n = 6):
            arr = [a[i:i+n] for i in range(0, len(a), n)]
            gameMap = [split(line) for line in arr]
            return gameMap

        def getCarName(car:vehicle):
            return car.name

        grid.map = splitString(str)


        #find all the
        allSymbolOnGrid = list(set(np.array(grid.map).flatten()))

        if '.' in allSymbolOnGrid:
            allSymbolOnGrid.remove('.')

        for carVal in allSymbolOnGrid:
            car = Car(carVal)
            startFound = False
            for i in range(len(grid.map)):
                for j in range(len(grid.map[i])):
                    if car.name == grid.map[i][j] and not startFound:
                        car.start = [i, j]
                        startFound = True
                    #keep iterating through the map until the last placement is found
                    elif car.name == grid.map[i][j]:
                        car.end = [i, j]
            startFound = False

            car.direction = 'horizontal' if (car.start[0] == car.end[0]) else 'vertical'
            grid.cars.append(car)

        #Sort cars by alphabetical order
        grid.cars = sorted(grid.cars, key=getCarName)


    def setGasLevel(grid, gasValues):
        for gas in gasValues:
            targetCar = gas[0]
            gasQty = int(gas[1:])
            car = grid.getCarByName(targetCar)
            car.gas = gasQty
