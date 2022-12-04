from Car import Car
from State import State
##do we need grids?

import queue as Q
from PriorityQueue import PriorityQueue as pq
from typing import List
import time



def UniformCostSearch(grid):
    OPEN = pq()
    CLOSED = []
    goalStates = []
    searchDetails = ''
    stateSearchCount = 0

    #Initial State
    initialState = State(cost = 0, grid = grid)
    subState = None

    OPEN.insert(initialState)
    searchDetails += initialState.getStateSearchDetail() + '\n'
    start_time = time.time()

    #Start search
    while True:
        #Check if no more options are left to be explored
        # print('OPEN size:', len(OPEN.queue) )
        # print('GoalState size:', len(goalStates) )

        #SUCCESS
        if len(goalStates) > 0:
            final_time = time.time() - start_time
            return subState, searchDetails, final_time, stateSearchCount

        #FAILURE
        if OPEN.isEmpty():
            final_time = time.time() - start_time
            return initialState, searchDetails, final_time, stateSearchCount

        #get leftMost state
        leftMostState = OPEN.get()

        CLOSED.append(leftMostState)
        #Check if goal state achieved for AA if yes, add to completedArray

        leftMostGrid = leftMostState.grid
        allMovements = leftMostGrid.getMoves()

        for soloMovement in allMovements:

            if len(goalStates) != 0:
                break

            for car, moves in soloMovement.items():
                car = Car(car)
                #iterate through all possible moves for a car
                for move in moves:

                    #Update the grid
                    subState = doMovement(leftMostState, car.name, move, searchDetails)


                    #Update the cost
                    prevG = leftMostState.g
                    newG = prevG + 1
                    subState.g = newG

                    #UCS cost is always edge cost --> g
                    subState.f = newG
                    subState.cost = newG

                    #Update searchDetails
                    searchDetails += subState.getStateSearchDetail() + '\n'

                    #CHECK IF IN CLOSED
                    openStateWithSameGridAsSubstate = checkForSameGridInOpen(OPEN, subState)
                    closedStateWithSameGridAsSubstate = checkForSameGridInClosed(CLOSED, subState)

                    #check if movement results into winning if not do state add to queue evaluation
                    if subState.grid.isGoalSpace():
                        goalStates.append(subState)
                        break

                    #add new subState if not same grid is found in the OPEN queue
                    elif openStateWithSameGridAsSubstate is None and closedStateWithSameGridAsSubstate is None: #would probably evaluate if same state already in OPEN but compare cost

                        # Count the amount of state change done
                        stateSearchCount += 1

                        OPEN.insert(subState)
                        #Check if substate has car possible for exit
                        subState.grid.removeExitCar()
                    else:
                        #if same grid found with lower cost, we ignore the new substate
                        #if same grid but higher cost, we add new one and discard the more expensive state from OPEN

                        if openStateWithSameGridAsSubstate is not None and subState.cost < openStateWithSameGridAsSubstate.cost:
                            # Count the amount of state change done
                            stateSearchCount += 1


                            #remove state from queue
                            OPEN.getState(openStateWithSameGridAsSubstate)
                            OPEN.insert(subState)

                        #Check if substate has car possible for exit
                        subState.grid.removeExitCar()


def GBFS(grid, heuristic):
    OPEN = pq()
    CLOSED = []
    goalStates = []
    searchDetails = ''
    #Initial State
    starting_heuristic = grid.heuristic(heuristic)
    initialState = State(cost = starting_heuristic, grid = grid)
    subState = None

    OPEN.insertH(initialState)
    start_time = time.time()
    searchDetails += subState.getStateSearchDetail() + '\n'

    #Start search
    while True:
        #Check if no more options are left to be explored
        # print('OPEN size:', len(OPEN.queue) )
        # print('GoalState size:', len(goalStates) )


        #SUCCESS
        if len(goalStates) > 0:
            final_time = time.time() - start_time
            return subState, searchDetails, final_time

        #FAILURE
        if OPEN.isEmpty():
            if len(goalStates) == 0:
                final_time = time.time() - start_time
                return initialState, searchDetails, final_time

        #get leftMost state
        leftMostState = OPEN.get()

        CLOSED.append(leftMostState)
        #Check if goal state achieved for AA if yes, add to completedArray

        leftMostGrid = leftMostState.grid
        allMovements = leftMostGrid.getMoves()

        for soloMovement in allMovements:

            if len(goalStates) != 0:
                break

            for car, moves in soloMovement.items():
                car = Car(car)
                #iterate through all possible moves for a car
                for move in moves:

                    #Update the grid
                    subState = doMovement(leftMostState, car.name, move, searchDetails)

                    #Update the cost


                    newCost = leftMostState.cost + 1
                    subState.cost = newCost
                    subState.h = subState.grid.heuristic(heuristic)

                    #Update searchDetails
                    searchDetails += subState.getStateSearchDetail() + '\n'

                    #would calculate heuristic here???
                    stateWithSameGridAsSubstate = checkForSameGridInOpen(OPEN, subState)
                    closedStateWithSameGridAsSubstate = checkForSameGridInClosed(CLOSED, subState)

                    #check if movement results into winning if not do state add to queue evaluation
                    if subState.grid.isGoalSpace():
                        goalStates.append(subState)
                        break

                    #add new subState if not same grid is found in the OPEN queue
                    elif stateWithSameGridAsSubstate is None and closedStateWithSameGridAsSubstate is None: #would probably evaluate if same state already in OPEN but compare cost
                        OPEN.insertH(subState)
                        #Check if substate has car possible for exit
                        subState.grid.removeExitCar()
                    else:
                        #if same grid found with lower cost, we ignore the new substate
                        #if same grid but higher cost, we add new one and discard the more expensive state from OPEN
                        if stateWithSameGridAsSubstate is not None and subState.cost < stateWithSameGridAsSubstate.cost:
                            #remove state from queue
                            OPEN.getState(stateWithSameGridAsSubstate)
                            OPEN.insertH(subState)
                        #Check if substate has car possible for exit
                        subState.grid.removeExitCar()


def findGoalStateWithLowestCost(goalStates:List[State]):
    lowestCostState = goalStates[0]
    for x in goalStates:
        if x.cost < lowestCostState.cost:
            lowestCostState = x

    return lowestCostState

def heuristic(grid,h):
        if(h == 'h1'):
            return grid.heuristicOne()
        elif(h =='h2'):
            return grid.heuristicTwo()
        elif(h=='h3'):
            return grid.heuristicThree()
        else:
            return grid.heuristicOne()


    def heuristicOne(grid):
        value = 0
        x = 5
        blockingCars = []
        while x > 0 :
                cell = grid.map[2][x]
                if cell == 'A':
                    x = 0
                    break
                elif not cell ==  '.':
                    if (cell not in blockingCars):
                        blockingCars.append(cell)
                        value +=1

                x -= 1
        return value

    def heuristicTwo(grid):
        value = 0
        x = 5
        while x > 0 :
                cell = grid.map[2][x]
                if cell == 'A':
                    x = 0
                    break
                elif not cell ==  '.':
                    value +=1

                x -= 1
        return value

    def heuristicThree(grid):
        multipler = 5 #Hard coded
        value = 0
        x = 5
        while x > 0 :
                cell = grid.map[2][x]
                if cell == 'A':
                    x = 0
                    break
                elif not cell ==  '.':
                    value +=1

                x -= 1
        return value * multipler
