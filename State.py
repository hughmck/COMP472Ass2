from Car import Car


class State:
    def __init__(self):
        self.gridSize = 6
        self.cars = []
        self.goal = [3, 6]
        self.prev = None
        self.cost = 0

    def puzzle_input(self):
        puzzle = "IJBBCCIJDDL.IJAAL.EEK.L...KFF..GGHH. F0 G6"  # need a single puzzle string as input
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
        board = self.build_board()
        for car in self.cars:
            if car.vert:
                for coord in car.occupy_square:
                    board[coord[0] - 1][coord[1] -1] = "."
        self.print_board()
        return board