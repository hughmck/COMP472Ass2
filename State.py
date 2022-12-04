from Car import Car


class State:
    def __init__(self): #grid will start at top left point 0,0 | top right
        self.gridSize = 6
        self.cars = []
        self.goal = [2, 5]
        self.prev = None
        self.cost = 0

    def puzzle_input(self):
        puzzle = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."  # need a single puzzle string as input
        print(puzzle)
        for index, l in enumerate(puzzle):
            if index < 36:
                if puzzle[index].isalpha() and index < 36:
                    # print(l + " is a letter")
                    if l in puzzle[0:index]:
                        for car in self.cars:
                            if l == car.name:
                                # print("This car already exists")
                                j = index % 6
                                i = index // 6
                                car.occupy_square.append((i, j))
                    else:
                        fuel = 100
                        removed = False
                        ambulance = False
                        name = l
                        # print("Car name is " + name)
                        occupy_square = []
                        j = index % 6
                        i = index // 6
                        occupy_square.append((i, j))
                        if name == 'A':
                            ambulance = True
                        if puzzle[index] == puzzle[index + 1]:
                            vert = False
                        else:
                            vert = True
                        self.cars.append(Car(occupy_square, vert, fuel, removed, ambulance, name))
                        # print("All cars in the list are: ")
                        # for car in self.cars:
                        #     print(car.name)

            else:
                # print("This is the gas setting section")
                try:
                    int(l)
                    # print("Is a number")
                    fuel = puzzle[index]
                    for car in self.cars:
                        if puzzle[index - 1] == car.name:
                            car.fuel = fuel
                            # print("The previous car letters was " + car.name)
                            # print("Car " + car.name + " has " + str(car.fuel) + " fuel left")
                except ValueError:
                    print("Checking fuel for car " + puzzle[index] + "\n")

        for car in self.cars:
            print("Details for car " + car.name + ":")
            if car.vert:
                print("Car " + car.name + " is Vertical")
            else:
                print("Car " + car.name + " is Horizontal")
            if car.ambulance:
                print("This is the ambulance")
            for coord in car.occupy_square:
                print("Car " + car.name + " is taking up squares " + str(coord[0]) + "," + str(coord[1]))
            print("Car " + car.name + " has " + str(car.fuel) + " fuel left \n")

    def build_board(self): #makes 2D array of spaces and pieces on the space
        board = [["."] * 6 for i in range(6)]
        for car in self.cars:
            for coord in car.occupy_square:
                board[coord[0]][coord[1]] = car.name
        return board

    def print_board(self):
        board = self.build_board()
        for i in board:
            print(i)
        print("\n")

    def get_moves(self):
        print("Coordinates work as (vertical, horizontal)")
        board = self.build_board()
        for car in self.cars:
            for coord in car.occupy_square:
                if car.vert:
                    if (coord[0] + 1) < 6 and board[coord[0] + 1][coord[1]] == ".":  #square below
                        print("The car " + car.name + " can move downwards from square " + str(coord[0]) + "," + str(coord[1]) + " to " + str(coord[0] + 1 ) + "," + str(coord[1]))
                    elif coord[0] + 1 >= 6:
                        print("The car " + car.name + " can not move to downwards from square " + str(coord[0]) + "," + str(coord[1]) + " as that move is out of bounds")
                    else:
                        print("The car " + car.name + " can not move downwards from square " + str(coord[0]) + "," + str(coord[1]) + " to " + str(coord[0] + 1) + "," + str(coord[1]))

                    if (coord[0] - 1) >= 0 and board[coord[0] - 1][coord[1]] == ".":  #square above
                        print("The car " + car.name + " can move upwards from square " + str(coord[0]) + "," + str(coord[1]) + " to " + str(coord[0] - 1 ) + "," + str(coord[1]))
                    elif coord[0] - 1 < 0:
                        print("The car " + car.name + " can not move to upwards from square " + str(coord[0]) + "," + str(coord[1]) + " as that move is out of bounds")
                    else:
                        print("The car " + car.name + " can not move upwards from square " + str(coord[0]) + "," + str(coord[1]) + " to " + str(coord[0] - 1) + "," + str(coord[1]))

                else:
                    if (coord[1] + 1) < 6 and board[coord[0]][coord[1] + 1] == ".": #square to the right
                        print("The car " + car.name + " can move to the right from square " + str(coord[0]) + "," + str(coord[1]) + " to " + str(coord[0]) + "," + str(coord[1] + 1))
                    elif coord[1] + 1 >= 6:
                        print("The car " + car.name + " can not move to the right from square " + str(coord[0]) + "," + str(coord[1]) + " as that move is out of bounds")
                    else:
                        print("The car " + car.name + " can not move to the right from square " + str(coord[0]) + "," + str(coord[1]) + " to " + str(coord[0]) + "," + str(coord[1] + 1))

                    if (coord[1] - 1) >= 0 and board[coord[0]][coord[1] - 1] == ".": #square to the left
                        print("The car " + car.name + " can move to the left from square " + str(coord[0]) + "," + str(coord[1]) + " to " + str(coord[0]) + "," + str(coord[1] - 1))
                    elif coord[1] - 1 < 0:
                        print("The car " + car.name + " can not move to the left from square " + str(coord[0]) + "," + str(coord[1]) + " as that move is out of bounds")
                    else:
                        print("The car " + car.name + " can not move to the left from square " + str(coord[0]) + "," + str(coord[1]) + " to " + str(coord[0]) + "," + str(coord[1] - 1))

        for i in board:
            print(i)
        print("\n")
        return board