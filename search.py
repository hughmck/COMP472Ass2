from ipaddress import v4_int_to_packed
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Initializing
    start=problem.getStartState()
    openlst = util.Stack()
    visited=[]
    #Push starting vertex into open stack
    openlst.push((start,[]))

    # While stack not empty
    while not openlst.isEmpty():
        # pop top vertex from stack
        current = openlst.pop()
        pos = current[0]
        path = current[1]

        # if goal node is reached then return the path
        if problem.isGoalState(pos):
            return path

        # if the current node is not in visited list
        if pos not in visited:
            # mark current node as explored
            visited.append(pos)
            # Generate neighbors of vertex
            neighbours = problem.getSuccessors(pos)

            # push current nodes neighbours into the openlist
            for x in neighbours:
                newpath = (x[0], path + [x[1]])
                openlst.push(newpath)


    # If stack empty then return empty path
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # Similar to DFS only change is Queue not Stack
    visited=[]
    start=problem.getStartState()
    openlst = util.Queue()
    openlst.push((start,[]))

    while not openlst.isEmpty():
        current = openlst.pop()
        pos = current[0]
        path = current[1]

        if problem.isGoalState(pos):
                return path

        if pos not in visited:
            visited.append(pos)
            neighbours = problem.getSuccessors(pos)
            for x in neighbours:
                newpath = (x[0], path + [x[1]])
                openlst.push(newpath)

    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Similar to DFS and BFS but uses Priority Queue and cost of actions to find lowest cost solution path
    start=problem.getStartState()
    openlst = util.PriorityQueue()
    visited=[]
    openlst.push((start,[]), 0)

    while not openlst.isEmpty():
        current = openlst.pop()
        pos = current[0]
        path = current[1]

        if problem.isGoalState(pos):
            return path

        if pos not in visited:
            visited.append(pos)
            neighbours = problem.getSuccessors(pos)

            for x in neighbours:
                newpos = x[0]
                newpath = path + [x[1]]
                cost = problem.getCostOfActions(newpath)
                newneighbour = (newpos, newpath)
                #push neighbour and cost into open list
                openlst.push(newneighbour, cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    '''
    g(n): distance between curr and start node
    h(n): estimated distance from curr to goal node
    f(n): total cost of node; start node to goal node
    '''
    start=problem.getStartState()
    openlst = util.PriorityQueue()
    visited=[]
    openlst.push((start,[]), 0)

    while not openlst.isEmpty():
        current = openlst.pop()
        pos = current[0]
        path = current[1]

        # returns path if current pos is the goal node
        goal=problem.isGoalState(pos)
        if goal:
            return path

        # push current pos node into visited if not visited
        if pos not in visited:
            visited.append(pos)
            neighbours = problem.getSuccessors(pos)
            # push current nodes neighbours into openlst if not visited
            for x in neighbours:
                if x[0] not in visited:
                    newpos = x[0]
                    newpath = path + [x[1]]
                    gn = problem.getCostOfActions(newpath)
                    hn = heuristic(newpos, problem)

                    fn = gn + hn
                    openlst.push((newpos, newpath), fn)

    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
