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
astar = aStarSearch
ucs = uniformCostSearch
