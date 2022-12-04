from Car import Car
from State import State

from PriorityQueue import PriorityQueue as pq
from typing import List
import time


def UniformCostSearch(grid): ##do we take grids as an argument or all moves?
    openStates = pq() ##initializing a priority queue of open nodes, will need to be constantly sorted
    closedStates = []
    goalStates = [] ##has the function reached a goal state? if yes, return
    initialState = State(cost = 0, grid = grid) ##initializing cost to 0 and trying to bring in the grid


    #adding the first initial state
    openStates.appendState(initialState)
    startingTime = time.time()

    #starting the search
    while len(goalStates) == 0:
        #was unable to find a solution
        if openStates.queueIsEmpty():
            totalRunTime = time.time()
            return initialState, totalRunTime, len(closedStates)

        if len(goalStates ==1) :
            totalRunTime = time.time()
            return totalRunTime, len(closedStates), State


        for i in allMoves    ##iterate through all moves in the state
        firstSearchState = allMoves[i]

        ##if cost is greater than comparison state add to closed state
        closedStates.append(firstSearchState)

        allMoves = State.getMoves()


def GBFS(grid, heuristic): ##GBFS also takes in a heuristic function
    openStates = pq() ##initializing a priority queue of open nodes, will need to be constantly sorted
    closedStates = []
    goalStates = [] ##has the function reached a goal state? if yes, return
    initialState = State(cost = 0, grid = grid) ##initializing cost to 0 and trying to bring in the grid


    #adding the first initial state
    openStates.appendState(initialState)
    startingTime = time.time()

    #starting the search
    while len(goalStates) == 0:
        #was unable to find a solution
        if openStates.queueIsEmpty():
            totalRunTime = time.time()
            return initialState, totalRunTime, len(closedStates)

        if len(goalStates ==1) :
            totalRunTime = time.time()
            return totalRunTime, len(closedStates), State


        for i in allMoves    ##iterate through all moves in the state
        firstSearchState = allMoves[i]

        ##if cost is greater than comparison state add to closed state
        closedStates.append(firstSearchState)

        allMoves = State.getMoves()

def a_star(grid, heuristic):
    openStates = pq() ##initializing a priority queue of open nodes, will need to be constantly sorted
    closedStates = []
    goalStates = [] ##has the function reached a goal state? if yes, return
    initialState = State(cost = 0, grid = grid) ##initializing cost to 0 and trying to bring in the grid

    #adding the first initial state
    openStates.appendState(initialState)
    startingTime = time.time()

    #starting the search
    while len(goalStates) == 0:
        #was unable to find a solution
        if openStates.queueIsEmpty():
            totalRunTime = time.time()
            return initialState, totalRunTime, len(closedStates)

        if len(goalStates ==1) :
            totalRunTime = time.time()
            return totalRunTime, len(closedStates), State


        for i in allMoves    ##iterate through all moves in the state
        firstSearchState = allMoves[i]

        ##if cost is greater than comparison state add to closed state
        closedStates.append(firstSearchState)

        allMoves = State.getMoves()
    return State, closed


def numberOfBlockingCars(grid):
    x = 5
    blockingCars = []
    blockedPositions = 0
    rightOfAmbulance = 5
    while rightOfAmbulance > 0 :
            cell = grid.map[2][rightOfAmbulance]
            if cell ==  '.':
                blockedPositions += 1
            else
                blockedPositions +=0
    return len(blockingCars)

def blockedPositions(grid):
    blockedPositions = 0
    rightOfAmbulance = 5
    while rightOfAmbulance > 0 :
            cell = grid.map[2][rightOfAmbulance]
            if cell ==  '.':
                blockedPositions += 0
                else
                blockedPositions +=1
    return blockedPositions

def blockedCarsMultiplied(grid):
    lm = 5
    x = 5
    blockingCars = []
    blockedPositions = 0
    rightOfAmbulance = 5
    while rightOfAmbulance > 0 :
            cell = grid.map[2][rightOfAmbulance]
            if cell ==  '.':
                blockedPositions += 1
            else
                blockedPositions +=0
    return x * lm
